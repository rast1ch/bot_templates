from aiogram import Router
from aiogram.types import CallbackQuery
from loguru import logger
from magic_filter import MagicFilter as F

from callbacks import MenuCallbackData
from enums import MenuItemsEnum


router = Router(name=__name__)


@router.callback_query(
    MenuCallbackData.filter(F().menu_item == MenuItemsEnum.INFO),
)
async def info_callback(
    query: CallbackQuery,
    callback_data: MenuCallbackData,
) -> None:
    if not query.bot:
        return
    logger.info(callback_data)
    await query.bot.send_message(query.from_user.id, "Loading...")
    await query.answer(
        "This is the information section. Here you can find more details about our services.",
    )
