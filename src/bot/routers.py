from aiogram import Router
from aiogram.filters import Command

from src.bot.handlers.help import help
from src.bot.handlers.start import message_router, start

main_router = Router()
_ = main_router.message.register(start, Command(commands=("start")))
_ = main_router.message.register(help, Command(commands=("help")))
_ = main_router.include_router(message_router)
