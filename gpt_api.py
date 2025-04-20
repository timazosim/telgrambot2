import openai
from config import settings

openai.api_key = settings.openai_api_key

async def ask_gpt(messages: list[dict]) -> str:
    response = await openai.ChatCompletion.acreate(
        model="gpt-3.5-turbo",
        messages=messages
    )
    return response.choices[0].message.content.strip()
