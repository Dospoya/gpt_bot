from aiogram import F, Router, types
from aiogram.filters import Command

from src.bot.dialoge_service import DialogService

message_router = Router()


async def start(message: types.Message, dialog_service: DialogService):
    user = message.from_user
    _ = await dialog_service.reset(user.id)
    if not user:
        return
    _ = await message.answer("Введите ваш вопрос")


@message_router.message(F.text, ~Command(commands=["start", "help"]))
async def message_handler(message: types.Message, dialog_service: DialogService):
    text = message.text
    if text is None:
        return
    answer = await dialog_service.handle_user_message(message.from_user.id, text)
    _ = await message.answer(f"Ответ на ваш вопрос: {answer}")
    _ = await message.answer("Введите ваш вопрос")
