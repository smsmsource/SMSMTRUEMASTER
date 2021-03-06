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
      InlineKeyboardButton(text="๐ ๐ฒ๐ป๐ ๐ฑ๏ธ", callback_data=f'stream_menu_panel | {user_id}'),
      InlineKeyboardButton(text="๐๐น๐ผ๐๐ฒ ๐๏ธ", callback_data=f'set_close'),
    ],
    [
      InlineKeyboardButton("[โฏ ๐อ๐ฒอ๐อ ๐ฆอ๐บอ๐ฆอ๐บอ ๐อ๐นอ๐อ๐ฏอ๐อ๐ฟอ - โฏ]๐๐๐๐ท๐ฃฉูููููููฐ โโ๐ฝ๐ฐ โฏ", callback_data="smsmelkbeer")
  ]
 ]
  return buttons


def menu_markup(user_id):
  buttons = [
    [
      InlineKeyboardButton(text="๐๐ก๐ โน", callback_data=f'set_stop | {user_id}'),
      InlineKeyboardButton(text="๐ฃ๐๐จ๐ฆ๐ โธ", callback_data=f'set_pause | {user_id}'),
      InlineKeyboardButton(text="๐ฅ๐๐ฆ๐จ๐ ๐ โถ๏ธ", callback_data=f'set_resume | {user_id}'),
    ],
    [
      InlineKeyboardButton(text="๐ ๐จ๐ง๐ ๐", callback_data=f'set_mute | {user_id}'),
      InlineKeyboardButton(text="๐จ๐ก ๐ ๐จ๐ง๐ ๐", callback_data=f'set_unmute | {user_id}'),
    ],
    [
      InlineKeyboardButton(text="[โฏ ๐อ๐ฒอ๐อ ๐ฆอ๐บอ๐ฆอ๐บอ ๐อ๐นอ๐อ๐ฏอ๐อ๐ฟอ - โฏ]๐๐๐๐ท๐ฃฉูููููููฐ โโ๐ฝ๐ฐ โฏ", callback_data='stream_home_panel'),
    ]
  ]
  return buttons


close_mark = InlineKeyboardMarkup(
  [
    [
      InlineKeyboardButton(
        "๐๐น๐ผ๐๐ฒ ๐๏ธ", callback_data="set_close"
      )
    ]
  ]
)


back_mark = InlineKeyboardMarkup(
  [
    [
      InlineKeyboardButton(
        "๐ ๐๐ผ ๐๐ฎ๐ฐ๐ธ", callback_data="stream_menu_panel"
      )
    ]
  ]
)
