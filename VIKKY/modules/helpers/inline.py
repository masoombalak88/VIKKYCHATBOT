from pyrogram.types import InlineKeyboardButton

from config import SUPPORT_GRP, UPDATE_CHNL
from VIKKY import BOT_USERNAME, OWNER

DEV_OP = [
    [
        InlineKeyboardButton(
            text="ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="🥀 ᴏᴡɴᴇʀ 🥀", user_id=OWNER),
        InlineKeyboardButton(text="sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{SUPPORT_GRP}"),
    ],
    [
        InlineKeyboardButton(text="ʜᴇʟᴘ ᴄᴏᴍᴍᴀɴᴅ", callback_data="HELP"),
    ],
]

####
PNG_BTN = [
    [
        InlineKeyboardButton(
            text="ᴀᴅᴅ ᴍᴇ",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
        InlineKeyboardButton(text="ᴜᴘᴅᴀᴛᴇ", url=f"https://t.me/{UPDATE_CHNL}"),
    ],
]

#####
BACK = [
    [
        InlineKeyboardButton(text="ʙᴀᴄᴋ", callback_data="BACK"),
    ],
]


####
HELP_BTN = [
    [
        InlineKeyboardButton(text="ʙᴀᴄᴋ", callback_data="BACK"),
        InlineKeyboardButton(text="ᴄʟᴏsᴇ", callback_data="CLOSE"),
    ],
]

#####
CLOSE_BTN = [
    [
        InlineKeyboardButton(text="ʀᴇᴘᴏ", url=f"https://t.me/its_vikky_ydv"),
        InlineKeyboardButton(text="ᴄʟᴏsᴇ", callback_data="CLOSE"),
    ],
]

####
CHATBOT_ON = [
    [
        InlineKeyboardButton(text="ᴇɴᴀʙʟᴇ", callback_data=f"addchat"),
        InlineKeyboardButton(text="ᴅɪsᴀʙʟᴇ", callback_data=f"rmchat"),
    ],
]

#####
CHATBOT_BACK = [
    [
        InlineKeyboardButton(text="ʙᴀᴄᴋ", callback_data="CHATBOT_BACK"),
        InlineKeyboardButton(text="ᴄʟᴏsᴇ", callback_data="CLOSE"),
    ],
]

####
HELP_START = [
    [
        InlineKeyboardButton(text="ʜᴇʟᴘ", callback_data="HELP"),
        InlineKeyboardButton(text="ᴄʟᴏsᴇ", callback_data="CLOSE"),
    ],
]

#####
HELP_BUTN = [
    [
        InlineKeyboardButton(
            text="ʜᴇʟᴘ", url=f"https://t.me/{BOT_USERNAME}?start=help"
        ),
        InlineKeyboardButton(text="ᴄʟᴏsᴇ", callback_data="CLOSE"),
    ],
]

######
