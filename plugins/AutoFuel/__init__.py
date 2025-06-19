from utils import *
from pyromod.exceptions import ListenerTimeout
# from pyrogram import Client, filters
from pyrogram import types
import asyncio


async def fuel_worker(app: Client, mod: Module):
    chat_str_id = "@bfgbunker_bot"
    chat_id = 5813222348
    while True:
        if not await mod.db.get('autofuel_enabled'):
            break
        
        await asyncio.sleep(0.1)
        try:
            response : types.messages_and_media.message.Message = await app.ask(
                                        chat_id=chat_id, text='Бензин', timeout=5)
        except ListenerTimeout:
            await app.send_message(chat_id=chat_id, text='Бот не отвечает(, поэтому автопополнение выключено')
            await mod.db.set('autofuel_enabled', False)
            return
        
        max_attempts = 3
        for attempt in range(max_attempts):
            try:
                await asyncio.sleep(0.1)
                await response.click("Купить бензин")
            except:
                pass
        await asyncio.sleep(360)
        

async def main(app: Client, mod: Module):
    
    cmd = mod.cmd
    
    @mod.on_ready
    async def _onr(_):
        if await mod.db.get('autofuel_enabled'):
            mod.add_task(fuel_worker(app, mod))
            app.logger.info("Autofuel автоматически включен")
    
    @cmd('autofuel')
    async def _autofuel(_, msg: M):
        if await mod.db.get('autofuel_enabled'):
            await mod.db.set('autofuel_enabled', False)
            app.logger.info("Автопополнение бензина выключено")
            return await msg.edit(f"Автопополнение бензина выключено!")
            
        await mod.db.set('autofuel_enabled', True)
        mod.add_task(fuel_worker(app, mod))
        app.logger.info("Автопополнение бензина включено")
        await msg.edit(f"Автопополнение бензина включено")
        