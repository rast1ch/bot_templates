from aiogram.filters.callback_data import CallbackData

from enums import MenuItemsEnum


class MenuCallbackData(CallbackData, prefix="menu"):
    menu_item: MenuItemsEnum
