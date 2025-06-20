from utils import *
from pyromod.exceptions import ListenerTimeout
from pyrogram import types
import asyncio
import re


class Emojis:
    V = '✅'
    X = '❌'

async def get_answer(text):
    pattern = r"🪴 Тебе доступна: [^\n]*\s([^\n]+)"

    match = re.search(pattern, text)

    answers = {
        "Картошка" : "картошку",
        "Морковь" : "морковь",
        "Рис" : "рис",
        "Свекла" : "свеклу",
        "Огурец" : "огурец",
        "Фасоль" : "фасоль",
        "Помидор" : "помидор",
    }
    return answers[match.group(1)]
    

async def greenhouse_worker(app: Client, mod: Module):
    chat_str_id = "@bfgbunker_bot"
    chat_id = 5813222348
    while True:
        if not await mod.db.get('autogreenhouse_enabled'):
            await mod.db.remove('autogreenhouse_get_text')
            break
        await asyncio.sleep(0.1)
        
        if not await mod.db.get('autogreenhouse_get_text', False):
            try:
                response : types.messages_and_media.message.Message = await app.ask(
                    chat_id=chat_id,
                    text="Моя теплица",
                    timeout=5
                )
            except ListenerTimeout:
                await app.bot.send_message(app.me.id, text=f"Autogreenhouse выключен{Emojis.X}")
                await mod.db.remove('autogreenhouse_get_text')
                await mod.db.set('autogreenhouse_enabled', False)
                break
            await mod.db.set('autogreenhouse_get_text', "вырастить " + await get_answer(response.text))
            await asyncio.sleep(2)
            
            pattern = r"💧\s*Вода:\s*(\d+)/"
            match = re.search(pattern, response.text)
            current_water = int(match.group(1))
            for i in range(current_water):
                await app.send_message(chat_id=chat_id, text=f"{await mod.db.get('autogreenhouse_get_text')}")
                mod.logger.info("Выращиваем в теплице на изначальную воду")
                await asyncio.sleep(2)
                if not await mod.db.get('autogreenhouse_enabled'):
                    await mod.db.remove('autogreenhouse_get_text')
                    return
            await asyncio.sleep(600)
        
        await app.send_message(chat_id=chat_id, text=f"{await mod.db.get('autogreenhouse_get_text')}")
        mod.logger.info("Выращиваем в теплице по таймеру")
        await asyncio.sleep(600)