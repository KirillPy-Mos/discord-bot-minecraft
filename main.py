import discord
from discord.ext import commands
from discord.ext.commands import *

token = ''

bot = commands.Bot(command_prefix='/', intents=discord.Intents.all())

@bot.event
async def of_ready():
    print("Запуск бота...")

@bot.event
async def on_message(message):
    if message.author.bot:
        return  
    print(f'Получено сообщение! Текст:\n{message.content}\nСервер:\n{message.guild}')


@bot.command()
async def help(ctx):
    await ctx.send("Это бот по Майнкрафту, и он тебе поможет")



bot.run()