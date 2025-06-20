from utils import *
from pyromod.exceptions import ListenerTimeout
from pyrogram import types
import asyncio

class Emojis:
    V = '✅'
    X = '❌'

async def fuel_worker(app: Client, mod: Module):
    chat_str_id = "@bfgbunker_bot"
    chat_id = 5813222348
    while True:
        if not await mod.db.get('autofuel_enabled'):
            break
        
        await asyncio.sleep(0.1)
        try:
            response : types.messages_and_media.message.Message = await app.ask(
                chat_id=chat_id, 
                text='Бензин',
                timeout=5
            )
        except ListenerTimeout:
            await app.bot.send_message(app.me.id, text=f"Autofuel выключен{Emojis.X}")
            await mod.db.set('autofuel_enabled', False)
            return
        
        max_attempts = 3
        for attempt in range(max_attempts):
            try:
                await asyncio.sleep(0.1)
                await response.click("Купить бензин")
            except:
                pass
        mod.logger.info("Пополняем бензин по таймеру")
        await asyncio.sleep(3200)