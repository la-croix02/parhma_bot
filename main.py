import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from keyboards import menu, q1_kb, q2_kb, q3_kb, q4_kb
from config import TOKEN, ADMIN_ID

from flask import Flask
from threading import Thread

# --- Flask для keep-alive ---
app = Flask('')

@app.route('/')
def home():
    return "Bot is running!"

def run():
    app.run(host='0.0.0.0', port=3000)

Thread(target=run).start()

# --- Telegram bot ---
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Хранилище ответов
user_answers = {}

# /start
@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer("Привет! Выберите действие:", reply_markup=menu)

# Кнопка "Пройти опрос"
@dp.message_handler(lambda message: message.text == "📝 Пройти опрос")
async def start_survey(message: types.Message):
    user_answers[message.from_user.id] = {}
    await message.answer("Вопрос 1: Вам удобно использовать нашу платформу?", reply_markup=q1_kb)

# Вопрос 1
@dp.message_handler(lambda message: message.text in ["Да", "Нет"])
async def answer_q1(message: types.Message):
    user_answers[message.from_user.id]["q1"] = message.text
    await message.answer("Вопрос 2: Что для вас важно?", reply_markup=q2_kb)

# Вопрос 2
@dp.message_handler(lambda message: message.text in ["Цена", "Доставка", "Ассортимент", "Консультация"])
async def answer_q2(message: types.Message):
    user_answers[message.from_user.id]["q2"] = message.text
    await message.answer("Вопрос 3: Какие категории препаратов вам интересны?", reply_markup=q3_kb)

# Вопрос 3
@dp.message_handler(lambda message: message.text in ["Витамины", "Обезболивающие", "Простуда", "Аллергия"])
async def answer_q3(message: types.Message):
    user_answers[message.from_user.id]["q3"] = message.text
    await message.answer("Вопрос 4: Будете ли вы рекомендовать нашу платформу?", reply_markup=q4_kb)

# Вопрос 4
@dp.message_handler(lambda message: message.text in ["Да", "Возможно", "Нет"])
async def answer_q4(message: types.Message):
    user_answers[message.from_user.id]["q4"] = message.text
    await message.answer("Спасибо за ваш фидбэк! ✅", reply_markup=menu)
    # Отправляем статистику админу
    await bot.send_message(
        ADMIN_ID,
        f"Новый опрос:\n{user_answers[message.from_user.id]}"
    )

# Старт бота
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)