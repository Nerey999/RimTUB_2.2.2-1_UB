from utils import *
from pyromod.exceptions import ListenerTimeout
from pyrogram import types
import asyncio
import re


class Emojis:
    V = '✅'
    X = '❌'

async def parse_bunker_stats(text):
    stats = {
        "in_bunker": 0,
        "in_queue": 0
    }
    
    bunker_match = re.search(r"🧍\s*Людей в бункере:\s*([\d,]+)", text)
    if bunker_match:
        stats["in_bunker"] = int(bunker_match.group(1).replace(",", ""))
    
    queue_match = re.search(r"↳\s*Людей в очереди в бункер:\s*(\d+)/", text)
    if queue_match:
        stats["in_queue"] = int(queue_match.group(1))
    
    return stats

async def people_worker(app: Client, mod: Module):
    chat_str_id = "@bfgbunker_bot"
    chat_id = 5813222348
    while True:
        if not await mod.db.get('autopeople_enabled'):
            break
        await asyncio.sleep(0.1)
        
        try:
            response : types.messages_and_media.message.Message = await app.ask(
                chat_id=chat_id,
                text="Б",
                timeout=5
            )
        except ListenerTimeout:
            await app.bot.send_message(app.me.id, text=f"Autopeople выключен{Emojis.X}")
            await mod.db.set('autofuel_enabled', False)
            return
        await asyncio.sleep(2)
        
        stats = await parse_bunker_stats(response.text)
        max_people = await mod.db.get('autopeople_max')

        if stats['in_bunker'] + stats['in_queue'] >= max_people:
            if max_people - stats['in_bunker'] > 0:
                await app.send_message(chat_id=chat_id, text=f"Впустить {max_people - stats['in_bunker']}")
            await app.bot.send_message(app.me.id, text=f"Autopeople выключен{Emojis.X}")
            await mod.db.set('autopeople_enabled', False)
            return
        
        if stats['in_queue'] != 0:
            await app.send_message(chat_id=chat_id, text=f"Впустить {stats['in_queue']}")
            mod.logger.info("Впускаем людей по таймеру")
        await asyncio.sleep(1800)
            
        
        