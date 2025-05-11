from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from callbacks.menu import MenuCallbackData
from enums import MenuItemsEnum


MENU_KEYBOARD = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="⚙️ Settings",
                callback_data=MenuCallbackData(
                    menu_item=MenuItemsEnum.SETTINGS,
                ).pack(),
            ),
            InlineKeyboardButton(
                text="❓ Info",
                callback_data=MenuCallbackData(
                    menu_item=MenuItemsEnum.INFO,
                ).pack(),
            ),
        ],
    ],
)
