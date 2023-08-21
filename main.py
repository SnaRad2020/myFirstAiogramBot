from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup
from dotenv import load_dotenv
import os


load_dotenv() #загрузка библиотеки dotenv в которой лежит токен и другие важные данные
bot = Bot('6159859028:AAFhenNkeG1SY1_MeanQKR1HilTqZjvBzi8')
dp = Dispatcher(bot=bot)
adm_id = int(os.getenv('ADMIN_ID'))
youtube_URL = os.getenv('URL')
email = os.getenv('EMAIL')

#Меню
main = ReplyKeyboardMarkup(resize_keyboard=True)
main.add('Наши песни').add('Контакты')


#Админ-меню
main_admin = ReplyKeyboardMarkup(resize_keyboard=True)
main_admin.add("Наши песни").add("Контакты").add("Админ-панель")


#Админ-панель
admin_panel = ReplyKeyboardMarkup(resize_keyboard=True)
admin_panel.add("Сделать рассылку").add("Добавить песню").add("Удалить песню").add("Назад")


#Команда /start
@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer_sticker(
        'CAACAgIAAxkBAAOCZNyhd7SU6MQLbGwCtiVCMYDFOJwAAtUiAAI68PhLqlYXuDuLjRMwBA')  # бот отправляет стикер перед приветствия
    await message.answer(f'Привет, {message.from_user.first_name}, я бот разработанный группой "Содержимое"',
                         reply_markup=main)
    if message.from_user.id == adm_id:
        await message.answer('Вы авторизовались, как администратор', reply_markup=main_admin)


#Команда ID
@dp.message_handler(text='ID')
async def ID(message: types.Message):
    await message.answer(f'{message.from_user.id}')


#Вход в админ-панель
@dp.message_handler(text='Админ-панель')
async def admin_panel_admin(message: types.Message):
    if message.from_user.id == adm_id:
        await message.answer(f'Вы вошли в админ-панель', reply_markup=admin_panel)
    else:
        await message.answer('Вы не авторизированы.')


#Наши песни
@dp.message_handler(text='Наши песни')
async def our_songs(message: types.Message):
    await message.answer(f'Наш YouTube канал: {youtube_URL}')


#Контакты
@dp.message_handler(text='Контакты')
async def contact_us(message: types.Message):
    await message.answer(f'Связаться с нами можно через Эл. почту {email}')


@dp.message_handler()
async def answer(message: types.Message):
    await message.reply('Я вас не понимаю.')

#executor
if __name__ == '__main__':
    executor.start_polling(dp)
