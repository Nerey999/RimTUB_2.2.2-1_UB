from utils import *
from pyromod.exceptions import ListenerTimeout
from pyrogram import types
import asyncio

from .autofuel import fuel_worker
from .autopeople import people_worker
from .autogreenhouse import greenhouse_worker

class Emojis:
    V = '✅'
    X = '❌'

async def main(app: Client, mod: Module):
    
    cmd = mod.cmd
    
    @mod.on_ready
    async def _onr(_):
        if await mod.db.get('autofuel_enabled'):
            mod.add_task(fuel_worker(app, mod))
            app.logger.info(f"Autofuel автоматически включен{Emojis.V}")
            await asyncio.sleep(4)
            
        if await mod.db.get('autopeople_enabled'):
            mod.add_task(people_worker(app, mod))
            app.logger.info(f"Autopeople автоматически включен{Emojis.V}")
            await asyncio.sleep(4)

        await mod.db.remove('autogreenhouse_get_text')    
        if await mod.db.get('autogreenhouse_enabled'):
            mod.add_task(greenhouse_worker(app, mod))
            app.logger.info(f"Greenhouse автоматически включен{Emojis.V}")
            await asyncio.sleep(4)
    
    @cmd('autocheck')
    async def _autocheck(_, msg: M):
        answer = ""
        answer += f"Автоматический бензин: {Emojis.V if await mod.db.get('autofuel_enabled') else Emojis.X}\n"
        max_people = await mod.db.get('autopeople_max')
        answer += f"Автоматические люди: {Emojis.V if await mod.db.get('autopeople_enabled') else Emojis.X} "\
                  f"{(max_people if max_people < 100000 else '∞') if await mod.db.get('autopeople_enabled') else ''}\n"
        answer += f"Автоматическая теплица: {Emojis.V if await mod.db.get('autogreenhouse_enabled') else Emojis.X}\n"
        await msg.edit_text(answer)
    
    @cmd('autofuel')
    async def _autofuel(_, msg: M):
        if await mod.db.get('autofuel_enabled'):
            await mod.db.set('autofuel_enabled', False)
            app.logger.info(f"Автопополнение бензина выключено{Emojis.X}")
            return await msg.edit(f"Автопополнение бензина выключено{Emojis.X}")

        await mod.db.set('autofuel_enabled', True)
        mod.add_task(fuel_worker(app, mod))
        app.logger.info(f"Автопополнение бензина включено{Emojis.V}")
        await msg.edit(f"Автопополнение бензина включено{Emojis.V}")
    
    @cmd('autopeople')
    async def _autopeople(_, msg: M):
        if await mod.db.get('autopeople_enabled'):
            await mod.db.set('autopeople_enabled', False)
            app.logger.info(f"Автоматические люди выключено{Emojis.X}")
            return await msg.edit(f"Автоматические люди выключено{Emojis.X}")
        
        request, args, kwargs = parse_args(get_args(msg.text))
        try:
            max_people = int(kwargs.get('-p', 1000000))
        except TypeError:
            await msg.edit_text("Тебе надо ввести число после флага -p")
            return
        except Exception as e:
            pass
        await mod.db.set('autopeople_max', max_people)
        
        await mod.db.set('autopeople_enabled', True)
        mod.add_task(people_worker(app, mod))
        app.logger.info(f"Автоматические люди включено{Emojis.V}")
        await msg.edit(f"Автоматические люди включено{Emojis.V}")
        
    
    @cmd('autogreenhouse')
    async def _autogreenhouse(_, msg: M):
        if await mod.db.get('autogreenhouse_enabled'):
            await mod.db.set('autogreenhouse_enabled', False)
            app.logger.info(f"Выращивание в теплице выключено{Emojis.X}")
            return await msg.edit(f"Выращивание в теплице выключено{Emojis.X}")

        await mod.db.set('autogreenhouse_enabled', True)
        mod.add_task(greenhouse_worker(app, mod))
        app.logger.info(f"Выращивание в теплице включено{Emojis.V}")
        await msg.edit(f"Выращивание в теплице включено{Emojis.V}")