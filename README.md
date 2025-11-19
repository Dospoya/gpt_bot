# request-gpt

Telegram-бот на базе `aiogram` и OpenAI (`gpt-4o-mini`), который:

- отвечает на команды `/start` и `/help`;
- пересылает текстовые сообщения в OpenAI и возвращает ответ;
- хранит историю диалога для каждого пользователя и использует её как контекст;
- сбрасывает контекст по команде `/start`.

Проект сейчас работает с **in-memory** хранилищем истории и спроектирован с возможностью расширения.

---

## Стек

- Python 3.13+
- [aiogram](https://docs.aiogram.dev/) `v3`
- [OpenAI Python SDK](https://github.com/openai/openai-python)
- pydantic / pydantic-settings
- ruff (линтер)
