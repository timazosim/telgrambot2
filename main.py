import asyncio
from aiogram import Bot, Dispatcher
from config import settings
from handlers import user
from utils.logger import setup_logger

async def main():
    setup_logger()
    bot = Bot(token=settings.bot_token)
    dp = Dispatcher()
    dp.include_router(user.router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
