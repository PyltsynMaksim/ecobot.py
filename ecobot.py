import discord

from discord.ext import commands
import os, random
import requests
bot = commands.Bot(command_prefix= '$', intents = discord.Intents.default())

@bot.event
async def on_read():
    print('I am working')

@bot.command()
async def mem(ctx):
    with open('images2/eco1.png', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def mem1(ctx):
    img_name = random.choice(os.listdir('images2'))
    with open(f'images2/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def list1(ctx):
    print('1. Сортируйте мусор')
    print('2. Займитесь облагораживанием своего города')
    print('3. Экономьте топливо')
    print('4. Снижайте потребление электроэнергии')
    print('5. Выбирайте правильные материалы')
    print('6. Экономьте воду')
    print('7. Не мусорьте')

@bot.command()
async def mem2(ctx):
    number = random.randint(1, 100)
    if  1 <= number >= 33:
        with open('images2/eco1.png', 'rb') as f:
            picture = discord.File(f)
    if 34 <= number >= 66:
        with open('images2/eco2.jpg', 'rb') as f:
            picture = discord.File(f)
    if 67 <= number >= 100:
        with open('images2/eco3.png', 'rb') as f:
            picture = discord.File(f)
    await ctx.send(file=picture)




bot.run("")
