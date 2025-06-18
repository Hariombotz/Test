from aiogram import types

async def handle_mood(message: types.Message):
    await message.reply("Tell me your mood today 🌈 (happy, sad, excited, etc.)")

async def handle_birthday(message: types.Message):
    await message.reply("When is your birthday? 🎂 (e.g. 12/06)")

async def respond_voice(message: types.Message):
    await message.reply("🎤 Voice replies coming soon (requires ffmpeg setup)")
