from typing import Any

from src.bot.service import create_request
from src.bot.storage.storage import DialogStorage


class DialogService:
    def __init__(self, storage: DialogStorage) -> None:
        self.storage = storage

    async def get_history(self, user_id: int) -> list[dict[str, Any]]:
        return await self.storage.get_history(user_id)

    async def handle_user_message(self, user_id: int, text: str):
        history: list[dict[str, Any]] = await self.get_history(user_id)
        user_prompt = {"role": "user", "content": text}
        history.append(user_prompt)
        instruction = [
            {"role": "system", "content": "Answer user questions clearly"}
        ] + history
        answer = await create_request(instruction)
        history.append({"role": "assistant", "content": answer})
        await self.storage.save(user_id, history)
        return answer

    async def reset(self, user_id: int):
        await self.storage.reset(user_id)
