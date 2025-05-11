from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from keyboards import MENU_KEYBOARD


router = Router(name=__name__)


@router.message(Command("start"))
@router.message(Command("menu"))
async def start_command(message: Message) -> None:
    await message.answer(
        "Hello! I'm your bot. How can I assist you today?",
        reply_markup=MENU_KEYBOARD,
    )
