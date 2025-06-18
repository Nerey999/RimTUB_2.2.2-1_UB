from utils import *

async def main(app: Client, mod: Module):

    cmd = mod.cmd
        
    @cmd('hello')
    async def _hello(_, msg: M):
        await msg.edit("ПРИВЕЕЕТ!!!")
