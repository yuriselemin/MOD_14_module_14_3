from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton




kb = ReplyKeyboardMarkup(
    [
        [KeyboardButton(text='Купить')]
    ],
    resize_keyboard=True
).row(KeyboardButton(text='Рассчитать'), KeyboardButton(text='Информация'))


menu_kb = InlineKeyboardMarkup()
menu_b1 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
menu_b2 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
menu_kb.add(menu_b1, menu_b2)


product_kb = InlineKeyboardMarkup()
product_b1 = InlineKeyboardButton(text='Саподилла', callback_data="product_buying")
product_b2 = InlineKeyboardButton(text='Чомпу', callback_data="product_buying")
product_b3 = InlineKeyboardButton(text='Аки', callback_data="product_buying")
product_b4 = InlineKeyboardButton(text='Амбарелла', callback_data="product_buying")
product_kb.add(product_b1, product_b2, product_b3, product_b4)