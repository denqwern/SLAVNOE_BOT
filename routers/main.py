import asyncio
import logging
import instaloader
from aiogram import Bot, Dispatcher, types
from routers import router as main_router
from aiogram import Router, F



BOT_TOKEN = "7181257781:AAE9AAtUcE7qgKvfe-aUTkMxARxSRqkFKS0"
API = '239cee0024050686ff009bb45541c0fa'
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
dp.include_router(main_router)
router = Router()



async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)






if __name__ == "__main__":
    asyncio.run(main())
