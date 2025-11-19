from aiogram import Bot
from aiogram.types import BotCommand


async def set_commands(bot: Bot) -> None:
    """Устанавливает список команд для Telegram-бота."""
    commands: list[BotCommand] = [
        BotCommand(command="start", description="Запустить бота"),
        BotCommand(command="help", description="Инструкция по использованию бота"),
    ]
    _ = await bot.set_my_commands(commands)
