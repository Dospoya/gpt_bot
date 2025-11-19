from aiogram import types


async def help(message: types.Message):
    user = message.from_user
    if not user:
        return
    _ = await message.answer("Помощь")
