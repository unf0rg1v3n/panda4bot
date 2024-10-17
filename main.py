import asyncio
import datetime
import logging
import os
import sys
import dotenv

from aiogram import Bot, Dispatcher
from aiogram.filters.command import Command

from weather_app import fetch_weather

import utils

dotenv.load_dotenv()

API_TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(API_TOKEN)
dp = Dispatcher(bot=bot)


@dp.message(Command('start'))
async def send_welcome(message):
    text = 'use\n/remind [dd.mm.yyyy] hh:mm [message]\nto set your remind'
    await message.reply(text)


@dp.message(Command('weather'))
async def get_weather(message):
    result = await fetch_weather()
    await message.reply(text=result)


@dp.message(Command('set'))
async def set_notification(message):
    chat_id = message.chat.id
    msg = message.text[4:]
    delay = utils.parse_date_from_message(msg)
    msg_to_notify = msg
    await send_reminder(chat_id, msg_to_notify, delay)


async def send_reminder(chat_id: int, message: str, delay: datetime):
    await asyncio.sleep(delay)
    await bot.send_message(chat_id=chat_id, text=message)


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
