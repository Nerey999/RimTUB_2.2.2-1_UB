import time
from utils import *
from utils import code as code_html
from pyrogram.types import Message
from .runner import CodeRunner, File

async def main(app: Client, mod: Module):
    
    runner = CodeRunner()
    
    @mod.cmd(["exec"])
    async def cmd_exec(_, msg: Message):
        await msg.edit(emoji(5328274090262275771, '🕐') + b(" Выполнение кода..."))
        try:
            _, lang, code_text = msg.text.split(maxsplit=2)
        except ValueError:
            await msg.edit(emoji(5447644880824181073, '⚠️') + b(" Вы не указали язык или код"))
            return

        try:
            t1 = time.time()
            result = await runner.execute(lang, [File(code_text)])
            t2 = time.time()
            await msg.edit(text=(
                f"{pre(code_text, lang)}\n"
                f"{code_html(result)}\n"
                f"{emoji(4985712614039355997, '🖥')} code>{lang}/code>\n"
                f"{emoji(5298728804074666786, '⏱')} {code(t2-t1)}"
            ))
        except Exception as err:
            await msg.edit(text=(
                    f"{emoji(5447644880824181073, '⚠️')} Произошла неизвестная ошибка, "
                    "возможно вы указали неверный язык"
                ))
            mod.logger.warning(f"Ошибка в модуле Code_textExecutor: {err}")
            
    @mod.cmd(["epy"])
    async def cmd_epy(_, msg: Message):
        await msg.edit(emoji(5328274090262275771, '🕐') + b(" Интерпретация кода..."))
        try:
            _, code_text = msg.text.split(maxsplit=1)
        except ValueError:
            await msg.edit(emoji(5447644880824181073, '⚠️') + b(" Вы не указали код!"))
            return

        try:
            t1 = time.time()
            result = await runner.execute("python3", [File(code_text)])
            t2 = time.time()
            await msg.edit(text=(
                f"{emoji(4985930888572306287, '🖥')} Python 3"
                f"{pre(code_text, 'py')}\n"
                f"{code_html(result)}\n"
                f"{emoji(5298728804074666786, '⏱')} {code(t2-t1)}"
            ))
        except Exception as err:
            await msg.edit(f"{emoji(5447644880824181073, '⚠️')} Произошла неизвестная ошибка")
            mod.logger.warning(f"Ошибка в модуле CodeExecutor: {err}", exc_info=True)
            
    @mod.cmd(["ejs"])
    async def cmd_ejs(_, msg: Message):
        await msg.edit(emoji(5328274090262275771, '🕐') + b(" Интерпретация кода..."))
        try:
            _, code_text = msg.text.split(maxsplit=1)
        except ValueError:
            await msg.edit(emoji(5447644880824181073, '⚠️') + b(" Вы не указали код!"))
            return

        try:
            t1 = time.time()
            result = await runner.execute("javascript", [File(code_text)])
            t2 = time.time()
            await msg.edit(text=(
                f"{emoji(4985930888572306287, '🖥')} JavaScript"
                f"{pre(code_text, 'js')}\n"
                f"{code_html(result)}\n"
                f"{emoji(5298728804074666786, '⏱')} {code(t2-t1)}"
            ))
        except Exception as err:
            await msg.edit(f"{emoji(5447644880824181073, '⚠️')} Произошла неизвестная ошибка")
            mod.logger.warning(f"Ошибка в модуле CodeExecutor: {err}")
            
    @mod.cmd(["elua"])
    async def cmd_elua(_, msg: Message):
        await msg.edit(emoji(5328274090262275771, '🕐') + b(" Интерпретация кода..."))
        try:
            _, code_text = msg.text.split(maxsplit=1)
        except ValueError:
            await msg.edit(emoji(5447644880824181073, '⚠️') + b(" Вы не указали код!"))
            return

        try:
            t1 = time.time()
            result = await runner.execute("lua", [File(code_text)])
            t2 = time.time()
            await msg.edit(text=(
                f"{emoji(4985930888572306287, '🖥')} Lua"
                f"{pre(code_text, 'lua')}\n"
                f"{code_html(result)}\n"
                f"{emoji(5298728804074666786, '⏱')} {code(t2-t1)}"
            ))
        except Exception as err:
            await msg.edit(f"{emoji(5447644880824181073, '⚠️')} Произошла неизвестная ошибка")
            mod.logger.warning(f"Ошибка в модуле CodeExecutor: {err}")
        
    @mod.cmd(["ecsh"])
    async def cmd_esh(_, msg: Message):
        await msg.edit(emoji(5328274090262275771, '🕐') + b(" Компиляция кода..."))
        try:
            _, code_text = msg.text.split(maxsplit=1)
        except ValueError:
            await msg.edit(emoji(5447644880824181073, '⚠️') + b(" Вы не указали код!"))
            return

        try:
            t1 = time.time()
            result = await runner.execute("csharp", [File(code_text)])
            t2 = time.time()
            await msg.edit(text=(
                f"{emoji(4985930888572306287, '🖥')} C#"
                f"{pre(code_text, 'cs')}\n"
                f"{code_html(result)}\n"
                f"{emoji(5298728804074666786, '⏱')} {code(t2-t1)}"
            ))
        except Exception as err:
            await msg.edit(f"{emoji(5447644880824181073, '⚠️')} Произошла неизвестная ошибка")
            mod.logger.warning(f"Ошибка в модуле CodeExecutor: {err}")
            
    @mod.cmd(["ec"])
    async def cmd_ec(_, msg: Message):
        await msg.edit(emoji(5328274090262275771, '🕐') + b(" Компиляция кода..."))
        try:
            _, code_text = msg.text.split(maxsplit=1)
        except ValueError:
            await msg.edit(emoji(5447644880824181073, '⚠️') + b(" Вы не указали код!"))
            return

        try:
            t1 = time.time()
            result = await runner.execute("c", [File(code_text)])
            t2 = time.time()
            await msg.edit(text=(
                f"{emoji(4985930888572306287, '🖥')} C"
                f"{pre(code_text, 'c')}\n"
                f"{code_html(result)}\n"
                f"{emoji(5298728804074666786, '⏱')} {code(t2-t1)}"
            ))
        except Exception as err:
            await msg.edit(f"{emoji(5447644880824181073, '⚠️')} Произошла неизвестная ошибка")
            mod.logger.warning(f"Ошибка в модуле CodeExecutor: {err}")

    @mod.cmd(["ecpp"])
    async def cmd_ecpp(_, msg: Message):
        await msg.edit(emoji(5328274090262275771, '🕐') + b(" Компиляция кода..."))
        try:
            _, code_text = msg.text.split(maxsplit=1)
        except ValueError:
            await msg.edit(emoji(5447644880824181073, '⚠️') + b(" Вы не указали код!"))
            return

        try:
            t1 = time.time()
            result = await runner.execute("c++", [File(code_text)])
            t2 = time.time()
            await msg.edit(text=(
                f"{emoji(4985930888572306287, '🖥')} C++"
                f"{pre(code_text, 'cpp')}\n"
                f"{code_html(result)}\n"
                f"{emoji(5298728804074666786, '⏱')} {code(t2-t1)}"
            ))
        except Exception as err:
            await msg.edit(f"{emoji(5447644880824181073, '⚠️')} Произошла неизвестная ошибка")
            mod.logger.warning(f"Ошибка в модуле CodeExecutor: {err}")

    @mod.cmd(["ers"])
    async def cmd_ers(_, msg: Message):
        await msg.edit(emoji(5328274090262275771, '🕐') + b(" Компиляция кода..."))
        try:
            _, code_text = msg.text.split(maxsplit=1)
        except ValueError:
            await msg.edit(emoji(5447644880824181073, '⚠️') + b(" Вы не указали код!"))
            return

        try:
            t1 = time.time()
            result = await runner.execute("rust", [File(code_text)])
            t2 = time.time()
            await msg.edit(text=(
                f"{emoji(4985930888572306287, '🖥')} Rust"
                f"{pre(code_text, 'rust')}\n"
                f"{code_html(result)}\n"
                f"{emoji(5298728804074666786, '⏱')} {code(t2-t1)}"
            ))
        except Exception as err:
            await msg.edit(f"{emoji(5447644880824181073, '⚠️')} Произошла неизвестная ошибка")
            mod.logger.warning(f"Ошибка в модуле CodeExecutor: {err}")

    @mod.cmd(["ejava"])
    async def cmd_epy(_, msg: Message):
        await msg.edit(emoji(5328274090262275771, '🕐') + b(" Выполнение кода..."))
        try:
            _, code_text = msg.text.split(maxsplit=1)
        except ValueError:
            await msg.edit(emoji(5447644880824181073, '⚠️') + b(" Вы не указали код!"))
            return

        try:
            t1 = time.time()
            result = await runner.execute("java", [File(code_text)])
            t2 = time.time()
            await msg.edit(text=(
                f"{emoji(4985930888572306287, '🖥')} Java"
                f"{pre(code_text, 'java')}\n"
                f"{code_html(result)}\n"
                f"{emoji(5298728804074666786, '⏱')} {code(t2-t1)}"
            ))
        except Exception as err:
            await msg.edit(f"{emoji(5447644880824181073, '⚠️')} Произошла неизвестная ошибка")
            mod.logger.warning(f"Ошибка в модуле CodeExecutor: {err}")
    