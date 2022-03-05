# Copyright (C) 2022 By SuraVCProject

from driver.core import me_bot, me_user
from driver.queues import QUEUE
from driver.decorators import check_blacklist
from program.utils.inline import menu_markup, stream_markup

from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from config import (
    BOT_USERNAME,
    BG_IMG,
    GROUP_SUPPORT,
    OWNER_USERNAME,
    UPDATES_CHANNEL,
    SUDO_USERS,
    OWNER_ID,
)



@Client.on_callback_query(filters.regex("arbic"))
async def arbic(_, query: CallbackQuery):
    await query.answer("home start")
    await query.edit_message_text(
        f"""مرحباً بك \n
⌁ ⁞  بوت تشغيل الأغاني والفيديو  في المكالمه ' المرئية
 البوت قيد التشغيل الان ⌯
⌁ ⁞ my developer [𝗦͛𝗲͛𝗠͛𝗼͛ 𝗘͛𝗟͛𝗸͛𝗕͛𝗲͛𝗥͛ ⌯](https://t.me/S_E_M_O_E_L_K_B_E_R)
⌁ ⁞  قم بإضافة البوت اللي مجموعتك واستمع إلى الموسيقى ومشاهدة الفيديوهات ⌯""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "- اضف البوت اللي مجموعتك -",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("- طريقة التفعيل -", callback_data="quick_use")],
                [
                    InlineKeyboardButton("- طريقة التشغيل -", callback_data="command_list"),
                    InlineKeyboardButton("- المطور -", url=f"https://t.me/{OWNER_NAME}"),
                ],
                [
                    InlineKeyboardButton(
                        "- الجروب -", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "- القناة -", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "𝗦͛𝗲͛𝗠͛𝗼͛ 𝗘͛𝗟͛𝗸͛𝗕͛𝗲͛𝗥͛ ⌯", url="https://t.me/S_E_M_O_E_L_K_B_E_R"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )

@Client.on_callback_query(filters.regex("english"))
async def english(_, query: CallbackQuery):
    await query.answer("home start")
    await query.edit_message_text(
        f"هنا لنكات تواصل  \n لو احتجت اي حاجه كلم المطور \n عن طريق الضغط علي تواصل واتساب \nاو الضغط علي اسم المطور ده➼ [𝗦͛𝗲͛𝗠͛𝗼͛ 𝗘͛𝗟͛𝗸͛𝗕͛𝗲͛𝗥͛ ⌯](https://t.me/S_E_M_O_E_L_K_B_E_R)",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "- اضف البوت الي مجموعتك -",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("- للتواصل واتساب -", url=f"http://wa.me/+201118106105")],
                [
                    InlineKeyboardButton("- جروب دردشه -", url=f"https://t.me/CC_G6"),
                    InlineKeyboardButton("- المطور -", url=f"https://t.me/{OWNER_NAME}"),
                ],
                [
                    InlineKeyboardButton(
                        "- جروب الدعم -", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "- قناه البوت -", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "𝗦͛𝗲͛𝗠͛𝗼͛ 𝗘͛𝗟͛𝗸͛𝗕͛𝗲͛𝗥͛ ⌯", url="https://t.me/S_E_M_O_E_L_K_B_E_R"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )    
    
@Client.on_callback_query(filters.regex("help_command"))
@check_blacklist()
async def help(_, query: CallbackQuery):
    BOT_NAME = me_bot.first_name
    await query.answer("help message")
    await query.edit_message_text(
        f""" ✨ **Hello [{query.message.chat.first_name}] !**\n
🔷 **To Know How to setup this Bot? Read 🤖 Setting Up This Bot in Group **\n
🔷 **To Know Play Video/Audio/Live? Read ✍️ Quick Use Commands **\n
🔷 **To Know Every Single Command Of Bot? Read 🎀 All Commands**\n """,
        reply_markup=InlineKeyboardMarkup(
        
        [
            [
                InlineKeyboardButton(
                    "🤖 Setting Up This Bot in Group", callback_data="user_guide"
                )
            ],
            [
                InlineKeyboardButton(
                    "✍️ Quick Use Commands", callback_data="quick_use"
                )
            ],
            [
                InlineKeyboardButton(
                    "🎀 All Commands", callback_data="command_list"
                )
            ],
            [
                InlineKeyboardButton(
                    "🔙 Go Back", callback_data="home_start"
                )
            ],
            [
                InlineKeyboardButton("👨🏾‍🤝‍👨🏼 Group", url=f"https://t.me/{GROUP_SUPPORT}"),
                InlineKeyboardButton(
                    "🔗 Channel", url=f"https://t.me/{UPDATES_CHANNEL}"
                ),
            ]
            
        ]      
  ),
    disable_web_page_preview=True,
    )
 

@Client.on_callback_query(filters.regex("quick_use"))
@check_blacklist()
async def quick_set(_, query: CallbackQuery):
    await query.answer("quick bot usage")
    await query.edit_message_text(
        f"""ℹ️ Quick use Guide bot, please read fully !

» /play - Type this with give the song title or youtube link or audio file to play Music. (Remember to don't play YouTube live stream by using this command!, because it will cause unforeseen problems.)

» /vplay - Type this with give the song title or youtube link or video file to play Video. (Remember to don't play YouTube live video by using this command!, because it will cause unforeseen problems.)

» /vstream - Type this with give the YouTube live stream video link or m3u8 link to play live Video. (Remember to don't play local audio/video files or non-live YouTube video by using this command!, because it will cause unforeseen problems.)

❓ Still Have questions? Contact us in [Support Group](https://t.me/{GROUP_SUPPORT}).""",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("🔙 Go Back to Bot Setup", callback_data="user_guide")],
                [InlineKeyboardButton("🔙 Go Back to Help", callback_data="help_command")]    
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("user_guide"))
@check_blacklist()
async def guide_set(_, query: CallbackQuery):
    await query.answer("user guide")
    await query.edit_message_text(
        f"""❓ How to Setup This Bot in Group ?, read the Guide below !

1.) First, add this bot to your Group.
2.) Then, promote this bot as administrator on the Group also give all permissions except Anonymous admin.
3.) After promoting this bot, type /reload in Group to update the admin data.
3.) Invite @{me_user.username} to your group or type /userbotjoin to invite her, unfortunately the userbot will joined by itself when you use song playing commands.
4.) Turn on/Start the video chat first before start to play video/music.

Read 
`- END, EVERYTHING HAS BEEN SETUP -`

📌 If the userbot not joined to video chat, make sure if the video chat already turned on and the userbot in the chat.

💡 If you have a follow-up questions about this bot, you can tell it on my support chat here: @{GROUP_SUPPORT}.""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("» Quick use Guide «", callback_data="quick_use")
                ],[
                    InlineKeyboardButton("🔙 Go Back to Start", callback_data="home_start")
                ],[
                    InlineKeyboardButton("🔙 Go Back to Help", callback_data="help_command")
                ]
            ]   
      ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("command_list"))
@check_blacklist()
async def commands_set(_, query: CallbackQuery):
    user_id = query.from_user.id
    await query.answer("commands menu")
    await query.edit_message_text(
        f"""✨ **Hello [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**

» Check out the menu below to read the module information & see the list of available Commands !

All commands can be used with (`! / .`) handler""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("👮🏻‍♀️ Admins Commands", callback_data="admin_command"),
                ],[
                    InlineKeyboardButton("👩🏻‍💼 Users Commands", callback_data="user_command"),
                ],[
                    InlineKeyboardButton("Sudo Commands", callback_data="sudo_command"),
                    InlineKeyboardButton("Owner Commands", callback_data="owner_command"),
                ],[
                    InlineKeyboardButton("🔙 Go Back to Start", callback_data="home_start")
                ],[
                    InlineKeyboardButton("🔙 Go Back to Help", callback_data="help_command")
                ]
                   
            ]
        ),
    )


@Client.on_callback_query(filters.regex("user_command"))
@check_blacklist()
async def user_set(_, query: CallbackQuery):
    BOT_NAME = me_bot.first_name
    await query.answer("basic commands")
    await query.edit_message_text(
        f"""✏️ Command list for all user.

» /play (song name/link) - play music on video chat
» /vplay (video name/link) - play video on video chat
» /vstream (m3u8/yt live link) - play live stream video
» /playlist - see the current playing song
» /lyric (query) - scrap the song lyric
» /video (query) - download video from youtube
» /song (query) - download song from youtube
» /search (query) - search a youtube video link
» /ping - show the bot ping status
» /uptime - show the bot uptime status
» /alive - show the bot alive info (in Group only)
» /help - to Show Help Message (Full Bot Guide)

⚡️ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="command_list")]]
        ),
    )


@Client.on_callback_query(filters.regex("admin_command"))
@check_blacklist()
async def admin_set(_, query: CallbackQuery):
    BOT_NAME = me_bot.first_name
    await query.answer("admin commands")
    await query.edit_message_text(
        f"""✏️ Command list for group admin.

» /pause - pause the current track being played
» /resume - play the previously paused track
» /skip - goes to the next track
» /stop - stop playback of the track and clears the queue
» /vmute - mute the streamer userbot on group call
» /vunmute - unmute the streamer userbot on group call
» /volume `1-200` - adjust the volume of music (userbot must be admin)
» /reload - reload bot and refresh the admin data
» /userbotjoin - invite the userbot to join group
» /userbotleave - order userbot to leave from group
» /startvc - start/restart the group call
» /stopvc - stop/discard the group call

⚡️ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="command_list")]]
        ),
    )


@Client.on_callback_query(filters.regex("sudo_command"))
@check_blacklist()
async def sudo_set(_, query: CallbackQuery):
    user_id = query.from_user.id
    BOT_NAME = me_bot.first_name
    if user_id not in SUDO_USERS:
        await query.answer("⚠️ You don't have permissions to click this button\n\n» This button is reserved for sudo members of this bot.", show_alert=True)
        return
    await query.answer("sudo commands")
    await query.edit_message_text(
        f"""✏️ Command list for sudo user.

» /stats - get the bot current statistic
» /calls - show you the list of all active group call in database
» /block (`chat_id`) - use this to blacklist any group from using your bot
» /unblock (`chat_id`) - use this to whitelist any group from using your bot
» /blocklist - show you the list of all blacklisted chat
» /speedtest - run the bot server speedtest
» /sysinfo - show the system informatio
» /logs - generate the current bot logs
» /eval - execute any code (`developer stuff`)
» /sh - run any command (`developer stuff`)

⚡ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="command_list")]]
        ),
    )


@Client.on_callback_query(filters.regex("owner_command"))
@check_blacklist()
async def owner_set(_, query: CallbackQuery):
    user_id = query.from_user.id
    BOT_NAME = me_bot.first_name
    if user_id not in OWNER_ID:
        await query.answer("⚠️ You don't have permissions to click this button\n\n» This button is reserved for owner of this bot.", show_alert=True)
        return
    await query.answer("owner commands")
    await query.edit_message_text(
        f"""✏️ Command list for bot owner.

» /gban (`username` or `user_id`) - for global banned people, can be used only in group
» /ungban (`username` or `user_id`) - for un-global banned people, can be used only in group
» /update - update your bot to latest version
» /restart - restart your bot directly
» /leaveall - order userbot to leave from all group
» /leavebot (`chat id`) - order bot to leave from the group you specify
» /broadcast (`message`) - send a broadcast message to all groups in bot database
» /broadcast_pin (`message`) - send a broadcast message to all groups in bot database with the chat pin

⚡ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="command_list")]]
        ),
    )


@Client.on_callback_query(filters.regex("stream_menu_panel"))
@check_blacklist()
async def at_set_markup_menu(_, query: CallbackQuery):
    user_id = query.from_user.id
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("❗ Only admin with manage video chat permission that can tap this button !", show_alert=True)
    chat_id = query.message.chat.id
    user_id = query.message.from_user.id
    buttons = menu_markup(user_id)
    if chat_id in QUEUE:
        await query.answer("control panel opened")
        await query.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))
    else:
        await query.answer("❌ nothing is currently streaming", show_alert=True)


@Client.on_callback_query(filters.regex("stream_home_panel"))
@check_blacklist()
async def is_set_home_menu(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("❗ Only admin with manage video chat permission that can tap this button !", show_alert=True)
    await query.answer("control panel closed")
    user_id = query.message.from_user.id
    buttons = stream_markup(user_id)
    await query.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))


@Client.on_callback_query(filters.regex("set_close"))
@check_blacklist()
async def on_close_menu(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("❗ Only admin with manage video chat permission that can tap this button !", show_alert=True)
    await query.message.delete()


@Client.on_callback_query(filters.regex("close_panel"))
@check_blacklist()
async def in_close_panel(_, query: CallbackQuery):
    await query.message.delete()

@Client.on_callback_query(filters.regex("ahmedelnqyb"))
async def ahmedelnqyb(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>◉ انا سيمو الكبير يمكنك التواصل معي..↑↓ \n\n◉ عن طريق معرفي اول جروب التواصل بلاسفل..↑↓ \n\n [𝗦͛𝗲͛𝗠͛𝗼͛ 𝗘͛𝗟͛𝗸͛𝗕͛𝗲͛𝗥͛ ⌯](https://t.me/S_E_M_O_E_L_K_B_E_R)</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("- القناة -", url=f"https://t.me/semo_elsultan2"),
                    InlineKeyboardButton("- الجروب -", url=f"https://t.me/SE_MO5"),
                ],
                [
                    InlineKeyboardButton("- جروب الدردشه -", url=f"https://t.me/CC_G6"),
                    InlineKeyboardButton("- تواصل واتساب -", url=f"http://wa.me/+201118106105"),
                ],
                [InlineKeyboardButton("𝗦͛𝗲͛𝗠͛𝗼͛ 𝗘͛𝗟͛𝗸͛𝗕͛𝗲͛𝗥͛ ⌯", url=f"https://t.me/S_E_M_O_E_L_K_B_E_R")],
            ]
        ),
    )
