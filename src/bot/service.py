import openai

from src.bot.config import settings

CLIENT = openai.AsyncClient(api_key=settings.gpt_token)


async def create_request(instruction: list[dict[str, str]]) -> str:
    response = await CLIENT.responses.create(model="gpt-4o-mini", input=instruction)
    return response.output_text
