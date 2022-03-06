import traceback

from pyrogram import Client
from pyrogram.errors import UserAlreadyParticipant, UserNotParticipant
from pyrogram.types import InlineKeyboardMarkup, Message

from pytgcalls import StreamType
from pytgcalls.types.input_stream import AudioPiped
from pytgcalls.types.input_stream.quality import HighQualityAudio
from pytgcalls.exceptions import NoAudioSourceFound, NoActiveGroupCall, GroupCallNotFound

from driver.decorators import require_admin, check_blacklist
from program.utils.inline import stream_markup
from driver.design.thumbnail import thumb
from driver.design.chatname import CHAT_TITLE
from driver.filters import command, other_filters
from driver.queues import QUEUE, add_to_queue
from driver.core import calls, user, me_user
from driver.utils import bash, remove_if_exists, from_tg_get_msg
from driver.database.dbqueue import add_active_chat, remove_active_chat, music_on
from config import BOT_USERNAME, IMG_5

from youtubesearchpython import VideosSearch


def ytsearch(query: str):
    try:
        search = VideosSearch(query, limit=1).result()
        data = search["result"][0]
        songname = data["title"]
        url = data["link"]
        duration = data["duration"]
        thumbnail = data["thumbnails"][0]["url"]
        return [songname, url, duration, thumbnail]
    except Exception as e:
        print(e)
        return 0

async def ytdl(link: str):
    stdout, stderr = await bash(
        f'yt-dlp --geo-bypass -g -f "best[height<=?720][width<=?1280]/best" {link}'
    )
    if stdout:
        return 1, stdout
    return 0, stderr


def convert_seconds(seconds):
    seconds = seconds % (24 * 3600)
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return "%02d:%02d" % (minutes, seconds)


async def play_tg_file(c: Client, m: Message, replied: Message = None, link: str = None):
    chat_id = m.chat.id
    user_id = m.from_user.id
    if link:
        try:
            replied = await from_tg_get_msg(link)
        except Exception as e:
            traceback.print_exc()
            return await m.reply_text(f"🚫 خطا:\n\n» {e}")
    if not replied:
        return await m.reply(
            "» الرجاء كتابه **اسم الاغنيه ** الصحيحه **والمحاوله مره اخري.**"
        )
    if replied.audio or replied.voice:
        if not link:
            suhu = await replied.reply("📥 تنزيل الصوت...")
        else:
            suhu = await m.reply("📥 تنزيل الصوت...")
        dl = await replied.download()
        link = replied.link
        songname = "music"
        thumbnail = f"{IMG_5}"
        duration = "00:00"
        try:
            if replied.audio:
                if replied.audio.title:
                    songname = replied.audio.title[:80]
                else:
                    songname = replied.audio.file_name[:80]
                if replied.audio.thumbs:
                    if not link:
                        thumbnail = await c.download_media(replied.audio.thumbs[0].file_id)
                    else:
                        thumbnail = await user.download_media(replied.audio.thumbs[0].file_id)
                duration = convert_seconds(replied.audio.duration)
            elif replied.voice:
                songname = "voice note"
                duration = convert_seconds(replied.voice.duration)
        except BaseException:
            pass

        if not thumbnail:
            thumbnail = f"{IMG_5}"

        if chat_id in QUEUE:
            await suhu.edit("🔄 مسار الانتظار...")
            gcname = m.chat.title
            ctitle = await CHAT_TITLE(gcname)
            title = songname
            userid = m.from_user.id
            image = await thumb(thumbnail, title, userid, ctitle)
            pos = add_to_queue(chat_id, songname, dl, link, "music", 0)
            requester = f"[{m.from_user.first_name}](tg://user?id={m.from_user.id})"
            buttons = stream_markup(user_id)
            await suhu.delete()
            await m.reply_video(
                video=f"https://telegra.ph/file/1bcec02263dae8300b63b.mp4",
                reply_markup=InlineKeyboardMarkup(buttons),
                caption=f"💡 **تمت إضافة المسار إلى قائمة الانتظار »** `{pos}`\n\n"
                        f"🗂 **الاسم:** [{songname}]({link}) | `music`\n"
                        f"⏱️ **المده:** `{duration}`\n"
                        f"🧸 **مطلوبه من:** {requester}",
            )
            remove_if_exists(image)
        else:
            try:
                gcname = m.chat.title
                ctitle = await CHAT_TITLE(gcname)
                title = songname
                userid = m.from_user.id
                image = await thumb(thumbnail, title, userid, ctitle)
                await suhu.edit("جاري التشغيل المساعد..⌯")
                await music_on(chat_id)
                await add_active_chat(chat_id)
                await calls.join_group_call(
                    chat_id,
                    AudioPiped(
                        dl,
                        HighQualityAudio(),
                    ),
                    stream_type=StreamType().pulse_stream,
                )
                add_to_queue(chat_id, songname, dl, link, "music", 0)
                await suhu.delete()
                buttons = stream_markup(user_id)
                requester = (
                    f"[{m.from_user.first_name}](tg://user?id={m.from_user.id})"
                )
                await m.reply_video(
                    video=f"https://telegra.ph/file/1bcec02263dae8300b63b.mp4",
                    reply_markup=InlineKeyboardMarkup(buttons),
                    caption=f"🗂 **الاسم:** [{songname}]({link}) | `music`\n"
                            f"⏱️ **المده:** `{duration}`\n"
                            f"🧸 **مطلوبه من:** {requester}",
                )
                remove_if_exists(image)
            except (NoActiveGroupCall, GroupCallNotFound):
                await suhu.delete()
                await remove_active_chat(chat_id)
                traceback.print_exc()
                await m.reply_text("❌ يتعذر على الروبوت العثور على مكالمة المجموعة أو أنه غير نشط.\n\n» استخدم الأمر لتشغيل المكالمة الجماعية ط ⌯ افتح ⌯ !")
            except BaseException as err:
                print(err)
    else:
        await m.reply(
            "» الرجاء كتابه  **اسم الاغنيه** الصحيح **وحاول البحث مجدداا.**"
        )


@Client.on_message(command(["/play", "play", f"play@{BOT_USERNAME}", "شغل", "تشغيل"]) & other_filters)
@check_blacklist()
@require_admin(permissions=["can_manage_voice_chats", "can_delete_messages", "can_invite_users"], self=True)
async def play(c: Client, m: Message):
    await m.delete()
    replied = m.reply_to_message
    chat_id = m.chat.id
    user_id = m.from_user.id
    if m.sender_chat:
        return await m.reply_text(
            "you're an __Anonymous__ user !\n\n» revert back to your real user account to use this bot."
        )
    try:
        ubot = me_user.id
        b = await c.get_chat_member(chat_id, ubot)
        if b.status == "banned":
            try:
                await m.reply_text("❌ تم حظر الحساب المساعد في هذه الدردشة ، قم بإلغاء حظر الحساب المسعد أولاً لتتمكن من تشغيل الموسيقى !")
                await remove_active_chat(chat_id)
            except BaseException:
                pass
            invitelink = (await c.get_chat(chat_id)).invite_link
            if not invitelink:
                await c.export_chat_invite_link(chat_id)
                invitelink = (await c.get_chat(chat_id)).invite_link
            if invitelink.startswith("https://t.me/+"):
                invitelink = invitelink.replace(
                    "https://t.me/+", "https://t.me/joinchat/"
                )
            await user.join_chat(invitelink)
            await remove_active_chat(chat_id)
    except UserNotParticipant:
        try:
            invitelink = (await c.get_chat(chat_id)).invite_link
            if not invitelink:
                await c.export_chat_invite_link(chat_id)
                invitelink = (await c.get_chat(chat_id)).invite_link
            if invitelink.startswith("https://t.me/+"):
                invitelink = invitelink.replace(
                    "https://t.me/+", "https://t.me/joinchat/"
                )
            await user.join_chat(invitelink)
            await remove_active_chat(chat_id)
        except UserAlreadyParticipant:
            pass
        except Exception as e:
            traceback.print_exc()
            return await m.reply_text(
                f"❌ **فشل الحساب المساعد في الانضمام**\n\n**السبب**: `{e}`"
            )
    if replied:
        if replied.audio or replied.voice:
            await play_tg_file(c, m, replied)
        else:
            if len(m.command) < 2:
                await m.reply(
                    "» الرجاء كتابه **اسم الاغنيه** or **الصحيح وحاول مره اخري**"
                )
            else:
                suhu = await c.send_message(chat_id, "💞 **جاري البحث انتظر ...**")
                query = m.text.split(None, 1)[1]
                search = ytsearch(query)
                if search == 0:
                    await suhu.edit("❌ **لم يتم العثور على نتائج**")
                else:
                    songname = search[0]
                    title = search[0]
                    url = search[1]
                    duration = search[2]
                    thumbnail = search[3]
                    userid = m.from_user.id
                    gcname = m.chat.title
                    ctitle = await CHAT_TITLE(gcname)
                    image = await thumb(thumbnail, title, userid, ctitle)
                    sura, ytlink = await ytdl(url)
                    if sura == 0:
                        await suhu.edit(f"❌ تم اكتشاف مشاكل في yt-dl\n\n» `{ytlink}`")
                    else:
                        if chat_id in QUEUE:
                            await suhu.edit("🔄 مسار الانتظار...")
                            pos = add_to_queue(
                                chat_id, songname, ytlink, url, "music", 0
                            )
                            await suhu.delete()
                            buttons = stream_markup(user_id)
                            requester = f"[{m.from_user.first_name}](tg://user?id={m.from_user.id})"
                            await m.reply_video(
                                video=f"https://telegra.ph/file/1bcec02263dae8300b63b.mp4",
                                reply_markup=InlineKeyboardMarkup(buttons),
                                caption=f"💡 **تمت إضافة المسار إلى قائمة الانتظار »** `{pos}`\n\n🗂 **الاسم:** [{songname}]({url}) | `music`\n**⏱ المده:** `{duration}`\n🧸 **مطلوبه من:** {requester}",
                            )
                            remove_if_exists(image)
                        else:
                            try:
                                await suhu.edit("🔄 جاري تشغيل المساعد...")
                                await music_on(chat_id)
                                await add_active_chat(chat_id)
                                await calls.join_group_call(
                                    chat_id,
                                    AudioPiped(
                                        ytlink,
                                        HighQualityAudio(),
                                    ),
                                    stream_type=StreamType().local_stream,
                                )
                                add_to_queue(chat_id, songname, ytlink, url, "music", 0)
                                await suhu.delete()
                                buttons = stream_markup(user_id)
                                requester = (
                                    f"[{m.from_user.first_name}](tg://user?id={m.from_user.id})"
                                )
                                await m.reply_video(
                                    video=f"https://telegra.ph/file/1bcec02263dae8300b63b.mp4",
                                    reply_markup=InlineKeyboardMarkup(buttons),
                                    caption=f"🗂 **الاسم:** [{songname}]({url}) | `music`\n**⏱ المده:** `{duration}`\n🧸 **مطلوبه من:** {requester}",
                                )
                                remove_if_exists(image)
                            except (NoActiveGroupCall, GroupCallNotFound):
                                await suhu.delete()
                                await remove_active_chat(chat_id)
                                await m.reply_text("❌ تمت إضافة المسار إلى قائمة الانتظار.\n\n» استخدم الأمر لتشغيل المكالمة الجماعية ⌯افتح⌯!")
                            except NoAudioSourceFound:
                                await suhu.delete()
                                await remove_active_chat(chat_id)
                                await m.reply_text("❌ المحتوى الذي تقدمه للتشغيل لا يحتوي على مصدر صوت")
                            except BaseException as err:
                                print(err)

    else:
        if len(m.command) < 2:
            await m.reply(
                "الرجاء كتابه **اسم الاغنيه** الصحيح **وحاول مجددا.**"
            )
        elif "t.me" in m.command[1]:
            for i in m.command[1:]:
                if "t.me" in i:
                    await play_tg_file(c, m, link=i)
                continue
        else:
            suhu = await c.send_message(chat_id, "💞 **جاري البحث انتظر...**")
            query = m.text.split(None, 1)[1]
            search = ytsearch(query)
            if search == 0:
                await suhu.edit("❌ **لم يتم العثور على نتائج**")
            else:
                songname = search[0]
                title = search[0]
                url = search[1]
                duration = search[2]
                thumbnail = search[3]
                userid = m.from_user.id
                gcname = m.chat.title
                ctitle = await CHAT_TITLE(gcname)
                image = await thumb(thumbnail, title, userid, ctitle)
                sura, ytlink = await ytdl(url)
                if sura == 0:
                    await suhu.edit(f"❌ تم اكتشاف مشاكل في yt-dl\n\n» `{ytlink}`")
                else:
                    if chat_id in QUEUE:
                        await suhu.edit("🔄 مسار الانتظار...")
                        pos = add_to_queue(chat_id, songname, ytlink, url, "music", 0)
                        await suhu.delete()
                        requester = f"[{m.from_user.first_name}](tg://user?id={m.from_user.id})"
                        buttons = stream_markup(user_id)
                        await m.reply_video(
                            video=f"https://telegra.ph/file/1bcec02263dae8300b63b.mp4",
                            reply_markup=InlineKeyboardMarkup(buttons),
                            caption=f"💡 **تمت إضافة المسار إلى قائمة الانتظار »** `{pos}`\n\n🗂 **الاسم:** [{songname}]({url}) | `music`\n**⏱ المده:** `{duration}`\n🧸 **مطلوبه من:** {requester}",
                        )
                        remove_if_exists(image)
                    else:
                        try:
                            await suhu.edit("🔄 جاري تشغيل المساعد...")
                            await music_on(chat_id)
                            await add_active_chat(chat_id)
                            await calls.join_group_call(
                                chat_id,
                                AudioPiped(
                                    ytlink,
                                    HighQualityAudio(),
                                ),
                                stream_type=StreamType().local_stream,
                            )
                            add_to_queue(chat_id, songname, ytlink, url, "music", 0)
                            await suhu.delete()
                            requester = f"[{m.from_user.first_name}](tg://user?id={m.from_user.id})"
                            buttons = stream_markup(user_id)
                            await m.reply_video(
                                video=f"https://telegra.ph/file/1bcec02263dae8300b63b.mp4",
                                reply_markup=InlineKeyboardMarkup(buttons),
                                caption=f"🗂 **الاسم:** [{songname}]({url}) | `music`\n**⏱ المده:** `{duration}`\n🧸 **مطلوبه من:** {requester}",
                            )
                            remove_if_exists(image)
                        except (NoActiveGroupCall, GroupCallNotFound):
                            await suhu.delete()
                            await remove_active_chat(chat_id)
                            await m.reply_text("❌ يتعذر على الروبوت العثور على مكالمة المجموعة أو أنه غير نشط.\n\n» استخدم الأمر لتشغيل المكالمة الجماعية ⌯افتح⌯!")
                        except NoAudioSourceFound:
                            await suhu.delete()
                            await remove_active_chat(chat_id)
                            await m.reply_text("❌ المحتوى الذي تقدمه للتشغيل لا يحتوي على مصدر صوت.\n\n» حاول تشغيل أغنية أخرى أو حاول مرة أخرى لاحقًا !")
                        except BaseException as err:
                            print(err)
