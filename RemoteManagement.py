import asyncio
import discord
from discord.ext import commands
import os

intents = discord.Intents.all()
intents.message_content = True
intents.reactions = True
bot = commands.Bot(command_prefix='/', intents=intents)

allowed_users = []#TODO

@bot.event
async def on_ready():
    print(f'{bot.user}准备就绪')

@bot.command()
async def startcmd(ctx):
    await ctx.send('远程cmd已启用，输入`/stopcmd`以禁用')
    asyncio.create_task(cmd_mode(ctx))

async def cmd_mode(ctx):
    while True:
        message = await bot.wait_for('message')
        if message.content.startswith('/stopcmd'):
            await ctx.send('远程Cmd已禁用')
            break
        result = await execute_command(message.content)
        await ctx.send(f"""```
{result}
                       ```""")

async def execute_command(command):
    try:
        parts = command.split(" ")
        if parts[0] == "cd":
            os.chdir(parts[1])
            return f"已切换至目录：{os.getcwd()}"
        else:
            process = await asyncio.create_subprocess_shell(
                command,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
                shell=True,
                encoding=None
            )
            stdout, stderr = await asyncio.wait_for(process.communicate(), timeout=10)
            output = stdout.strip() if stdout else stderr.strip()
            result = f"{os.getcwd()}:\n{output.decode('ansi')}"
            return result
    except asyncio.TimeoutError:
        return "命令执行超时"
    except Exception as e:
        return str(e)

bot.run('')
