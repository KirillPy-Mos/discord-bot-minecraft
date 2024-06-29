import discord
from discord.ext import commands
from discord.ext.commands import *
from discord.ui import *

token = ''

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="*", intents=intents)

class MyView(discord.ui.View):
    def __init__(self, url):
        super().__init__()

        self.add_item(Button(label="Нажми", url=url))

@bot.event
async def of_ready():
    print("Запуск бота...")


@bot.command()
async def help_bot(ctx):
    await ctx.send("Это бот по Майнкрафту, и он тебе поможет")

@bot.command()
async def open_sourse(ctx):
    await ctx.send("Ссылка на Github: https://github.com/KirillPy-Mos/discord-bot-minecraft")

@bot.command()
async def wiki(ctx, *, what):
    what = what.lower()
    if what == "майнкрайт" or "minecraft":
        view = MyView("https://minecraft.fandom.com/ru/wiki/Minecraft")
        await ctx.send("Вот ссылка на википедию", view = view) 
        return
    if what == "java edition" or "джава версия":
        view = MyView("https://minecraft.fandom.com/ru/wiki/Java_Edition")
        await ctx.send("Вот ссылка на википедию", view = view)
        return

bot.run(token)