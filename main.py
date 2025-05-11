import asyncio

from aiogram import Bot, Dispatcher

from container import MainContainer
from routers import router as main_router
from settings import settings
from utils import on_shutdown, on_startup


bot = Bot(token=settings.BOT_TOKEN)
dp = Dispatcher()


async def main(bot: Bot, dp: Dispatcher) -> tuple[Bot, Dispatcher]:
    try:
        MainContainer()
        on_startup()
        dp.include_router(main_router)
        await dp.start_polling(bot)
    except KeyboardInterrupt:
        on_shutdown()
        return bot, dp
    return bot, dp


if __name__ == "__main__":
    asyncio.run(main(bot, dp))
