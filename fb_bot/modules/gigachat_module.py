from gigachat import GigaChat

from fb_bot.config import GIGA_TOKEN


async def get_text(prompt: str):
    giga = GigaChat(credentials=GIGA_TOKEN, scope='GIGACHAT_API_PERS', verify_ssl_certs=False)
    response = await giga.achat(prompt)
    return response.choices[0].message.content
