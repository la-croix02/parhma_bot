import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import Command
from config import TOKEN, ADMIN_ID
from keyboards import menu, q1_kb, q2_kb, q3_kb, q4_kb
from database import save_survey, get_stats, get_total

bot = Bot(token=TOKEN)
dp = Dispatcher()

user_data = {}  # временные данные пользователя

@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "Добро пожаловать!\nМы собираем фидбэк о будущей онлайн-аптеке.",
        reply_markup=menu
    )

# Начало опроса
@dp.message(F.text == "📝 Пройти опрос")
async def survey_start(message: Message):
    user_data[message.from_user.id] = {}
    await message.answer("Вопрос 1/4:\nПользовались ли вы онлайн-аптеками?", reply_markup=q1_kb)

# Вопрос 1
@dp.message(lambda msg: msg.from_user.id in user_data and "q1" not in user_data[msg.from_user.id])
async def q1(message: Message):
    user_data[message.from_user.id]["q1"] = message.text
    await message.answer("Вопрос 2/4:\nЧто для вас важнее всего?", reply_markup=q2_kb)

# Вопрос 2
@dp.message(lambda msg: msg.from_user.id in user_data and "q2" not in user_data[msg.from_user.id])
async def q2(message: Message):
    user_data[message.from_user.id]["q2"] = message.text
    await message.answer("Вопрос 3/4:\nКакие категории покупаете чаще?", reply_markup=q3_kb)

# Вопрос 3
@dp.message(lambda msg: msg.from_user.id in user_data and "q3" not in user_data[msg.from_user.id])
async def q3(message: Message):
    user_data[message.from_user.id]["q3"] = message.text
    await message.answer("Вопрос 4/4:\nБудете ли пользоваться таким сервисом?", reply_markup=q4_kb)

# Вопрос 4 + сохранение
@dp.message(lambda msg: msg.from_user.id in user_data and "q4" not in user_data[msg.from_user.id])
async def q4(message: Message):
    user_data[message.from_user.id]["q4"] = message.text
    data = user_data[message.from_user.id]
    save_survey(message.from_user.id, data["q1"], data["q2"], data["q3"], data["q4"])
    await message.answer("Спасибо за участие!", reply_markup=menu)
    del user_data[message.from_user.id]

# Админ: статистика
@dp.message(Command("stats"))
async def stats(message: Message):
    if message.from_user.id != ADMIN_ID:
        return
    stats_data = get_stats()
    total = get_total()
    text = f"📊 Статистика опроса\nВсего ответов: {total}\n\n"
    questions = {
        "q1": "Пользовались онлайн-аптеками",
        "q2": "Что важнее",
        "q3": "Категории",
        "q4": "Будут пользоваться"
    }
    for q in stats_data:
        text += questions[q] + ":\n"
        for row in stats_data[q]:
            text += f"{row[0]} — {row[1]}\n"
        text += "\n"
    await message.answer(text)

# Запуск
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())