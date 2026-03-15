from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Главное меню
menu = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton("📝 Пройти опрос")]],
    resize_keyboard=True
)

# Вопрос 1
q1_kb = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton("Да"), KeyboardButton("Нет")]],
    resize_keyboard=True,
    one_time_keyboard=True
)

# Вопрос 2
q2_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton("Цена"), KeyboardButton("Доставка")],
        [KeyboardButton("Ассортимент"), KeyboardButton("Консультация")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

# Вопрос 3
q3_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton("Витамины"), KeyboardButton("Обезболивающие")],
        [KeyboardButton("Простуда"), KeyboardButton("Аллергия")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

# Вопрос 4
q4_kb = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton("Да"), KeyboardButton("Возможно"), KeyboardButton("Нет")]],
    resize_keyboard=True,
    one_time_keyboard=True
)