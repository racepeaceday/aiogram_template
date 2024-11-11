import asyncio

from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram.filters.command import Command

from app.loader import bot, dp

from app import config

@dp.message(Command(commands=['start']))
async def start_menu_handler(message: Message):
    await message.answer(
        reply_to_message_id=message.message_id,
        text=message.html_text
    )