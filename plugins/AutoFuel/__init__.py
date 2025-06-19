from utils import *
from pyromod.exceptions import ListenerTimeout
# from pyrogram import Client, filters
from pyrogram import types

async def main(app: Client, mod: Module):
    
    cmd = mod.cmd
    
    @mod.on_ready
    async def _onr(_):
        pass
    
    @cmd('autofuel')
    async def _autofuel(_, msg: M):
        chat_str_id = "@bfgbunker_bot"
        chat_id = 5813222348
        
        try:
            response : types.messages_and_media.message.Message = await app.ask(chat_id=chat_id, text='Бензин', timeout=5)
        except ListenerTimeout:
            await msg.reply('Бот не отвечает(')
            return
        
        await response.click(0, 0)
        