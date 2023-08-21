from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton


#Меню
main = ReplyKeyboardMarkup(resize_keyboard=True)
main.add('Наши песни').add('Контакты')


#Админ-меню
main_admin = ReplyKeyboardMarkup(resize_keyboard=True)
main_admin.add("Наши песни").add("Контакты").add("Админ-панель")


#Админ-панель
admin_panel = ReplyKeyboardMarkup(resize_keyboard=True)
admin_panel.add("Сделать рассылку").add("Добавить песню").add("Удалить песню").add("Назад")
#Список песен
song_list = InlineKeyboardMarkup(row_width=1)
song_list.add(
    InlineKeyboardButton(text='Бананафилы', url='https://www.youtube.com/watch?v=K7fWE2dDsRE&ab'),
    InlineKeyboardButton(text='Пёс Барбос', url='https://www.youtube.com/watch?v=PFsMwaeV8Mk&ab'),
    InlineKeyboardButton(text='Каждый день', url='https://www.youtube.com/watch?v=6h2fVZ70ytI&ab')
)