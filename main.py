import asyncio

from aiogram import Bot, Dispatcher

from routers import router as main_router
from settings import settings


bot = Bot(token=settings.BOT_TOKEN)
dp = Dispatcher()


async def main(bot: Bot, dp: Dispatcher) -> tuple[Bot, Dispatcher]:
    try:
        dp.include_router(main_router)
        await dp.start_polling(bot)
    except KeyboardInterrupt:
        print("on_shutdown")
        print("Bot stopped by user.")
        return bot, dp
    return bot, dp


if __name__ == "__main__":
    asyncio.run(main(bot, dp))
