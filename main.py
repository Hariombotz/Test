import logging
from aiogram import Bot, Dispatcher, executor, types
from config import BOT_TOKEN, ADMIN_ID
from utils import handle_mood, handle_birthday, respond_voice

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def send_welcome(message: types.Message):
    await message.reply("""Hey bestie! 💖 I'm Ananya, your BFF chatbot!""")

@dp.message_handler(commands=["mood"])
async def mood_checkin(message: types.Message):
    await handle_mood(message)

@dp.message_handler(commands=["birthday"])
async def birthday_save(message: types.Message):
    await handle_birthday(message)

@dp.message_handler(commands=["voice"])
async def send_voice(message: types.Message):
    await respond_voice(message)

@dp.message_handler(commands=["hug"])
async def hug_reply(message: types.Message):
    await message.reply("🤗 Sending you a big hug, bestie!")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
