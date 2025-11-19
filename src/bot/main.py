from aiogram import Bot, Dispatcher

from src.bot.config import settings
from src.bot.dialoge_service import DialogService
from src.bot.routers import main_router
from src.bot.storage.storage import InMemoryDialogStorage
from src.bot.utils import set_commands

storage = InMemoryDialogStorage()
dialog_service = DialogService(storage)
bot = Bot(token=settings.bot_token)
dp = Dispatcher()
_ = dp.include_router(main_router)


async def main() -> None:
    await set_commands(bot)
    dp["dialog_service"] = dialog_service
    await dp.start_polling(bot)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
