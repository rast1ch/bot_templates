from aiogram import Router
from aiogram.types import CallbackQuery
from magic_filter import MagicFilter as F

from loguru import logger
from callbacks import MenuCallbackData
from enums import MenuItemsEnum


router = Router(name=__name__)


@router.callback_query(
    MenuCallbackData.filter(F().menu_item == MenuItemsEnum.SETTINGS),
)
async def settings_callback(
    query: CallbackQuery,
    callback_data: MenuCallbackData,
) -> None:
    if not query.bot:
        return
    logger.info(
        callback_data,
    )
    await query.bot.send_message(query.from_user.id, "Loading settings...")
    await query.answer(
        "This is the settings section. Here you can adjust your preferences.",
    )
