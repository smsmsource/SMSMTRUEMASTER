""" inline section button """

from config import BOT_USERNAME
from pyrogram.types import (
  CallbackQuery,
  InlineKeyboardButton,
  InlineKeyboardMarkup,
  Message,
)


def stream_markup(user_id):
  buttons = [
    [
      InlineKeyboardButton(text="𝗠𝗲𝗻𝘂 🖱️", callback_data=f'stream_menu_panel | {user_id}'),
      InlineKeyboardButton(text="𝗖𝗹𝗼𝘀𝗲 🗑️", callback_data=f'set_close'),
    ],
    [
      InlineKeyboardButton("𝗦͛𝗲͛𝗠͛𝗼͛ 𝗘͛𝗟͛𝗸͛𝗕͛𝗲͛𝗥͛ ⌯", callback_data="ahmedelnqyb")
  ]
 ]
  return buttons


def menu_markup(user_id):
  buttons = [
    [
      InlineKeyboardButton(text="𝗘𝗡𝗗 ⏹", callback_data=f'set_stop | {user_id}'),
      InlineKeyboardButton(text="𝗣𝗔𝗨𝗦𝗘 ⏸", callback_data=f'set_pause | {user_id}'),
      InlineKeyboardButton(text="𝗥𝗘𝗦𝗨𝗠𝗘 ▶️", callback_data=f'set_resume | {user_id}'),
    ],
    [
      InlineKeyboardButton(text="𝗠𝗨𝗧𝗘 🔇", callback_data=f'set_mute | {user_id}'),
      InlineKeyboardButton(text="𝗨𝗡 𝗠𝗨𝗧𝗘 🔊", callback_data=f'set_unmute | {user_id}'),
    ],
    [
      InlineKeyboardButton(text="[⌯ 𝗗͛𝗲͛𝘃͛ 𝗦͛𝗺͛𝗦͛𝗺͛ 𝗘͛𝗹͛𝗞͛𝗯͛𝗘͛𝗿͛ - ⌯]𝟏𝟎𝐊🍷𖣩ًََِْٰٓ ⃝⃙🇽🇰 ⌯", callback_data='stream_home_panel'),
    ]
  ]
  return buttons


close_mark = InlineKeyboardMarkup(
  [
    [
      InlineKeyboardButton(
        "𝗖𝗹𝗼𝘀𝗲 🗑️", callback_data="set_close"
      )
    ]
  ]
)


back_mark = InlineKeyboardMarkup(
  [
    [
      InlineKeyboardButton(
        "🔙 𝗚𝗼 𝗕𝗮𝗰𝗸", callback_data="stream_menu_panel"
      )
    ]
  ]
)
