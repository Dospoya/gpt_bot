from collections import defaultdict
from typing import Any, override


class DialogStorage:
    async def reset(self, user_id) -> None:
        raise NotImplementedError

    async def get_history(self, user_id: int) -> list[dict[str, Any]]:
        raise NotImplementedError

    async def save(self, user_id: int, history: list[dict[str, Any]]) -> None:
        raise NotImplementedError


class InMemoryDialogStorage(DialogStorage):
    def __init__(self) -> None:
        self._store: dict[int, list[dict[str, Any]]] = defaultdict(list)

    @override
    async def save(self, user_id: int, history: list[dict[str, Any]]):
        self._store[user_id] = history

    @override
    async def get_history(self, user_id: int) -> list[dict[str, Any]]:
        return self._store[user_id]

    @override
    async def reset(self, user_id: int) -> None:
        if user_id in self._store:
            del self._store[user_id]
