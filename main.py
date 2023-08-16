from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import os

load_dotenv()
bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer(f'Привет, {message.from_user.first_name}, я бот разработанный для обучения')


@dp.message_handler()
async def answer(message: types.Message):
    await message.reply('Я вас не понимаю.')


if __name__ == '__main__':
    executor.start_polling(dp)
