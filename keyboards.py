from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Главное меню
menu = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="📝 Пройти опрос")]],
    resize_keyboard=True
)

# Варианты ответов для каждого вопроса
q1_kb = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="Да"), KeyboardButton(text="Нет")]],
    resize_keyboard=True,
    one_time_keyboard=True
)

q2_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Цена"), KeyboardButton(text="Доставка")],
        [KeyboardButton(text="Ассортимент"), KeyboardButton(text="Консультация")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

q3_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Витамины"), KeyboardButton(text="Обезболивающие")],
        [KeyboardButton(text="Простуда"), KeyboardButton(text="Аллергия")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

q4_kb = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="Да"), KeyboardButton(text="Возможно"), KeyboardButton(text="Нет")]],
    resize_keyboard=True,
    one_time_keyboard=True
)