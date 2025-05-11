from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


MENU_KEYBOARD = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="📊 Statistics",
                callback_data="menu:statistics",
            ),
            InlineKeyboardButton(
                text="🗂️ Files",
                callback_data="menu:files",
            ),
        ],
        [
            InlineKeyboardButton(
                text="⚙️ Settings",
                callback_data="menu:settings",
            ),
            InlineKeyboardButton(
                text="❓ Help",
                callback_data="menu:help",
            ),
        ],
    ],
)
