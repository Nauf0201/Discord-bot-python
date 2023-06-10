import discord
from discord.ext import commands

# try :
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

#List of trash can

trash_list_o = ['Leaf', 'fruit', 'Dirt']

trash_list_a = ['Plastic', 'Bottle', 'Tissue']

trash_list_b = ['Battery', 'Lamp', 'Drug']

#on command

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

#Hello

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

#emotion

@bot.command()
async def smile(ctx):
    await ctx.send(f':D')

@bot.command()
async def cry(ctx):
    await ctx.send(f':_(')

#Calculator

@bot.command()
async def plus(ctx, letter_1, letter_2):
    await ctx.send(int(letter_1) + int(letter_2))

@bot.command()
async def multiply(ctx, number_1, number_2):
    await ctx.send(int(number_1) * int(number_2))

@bot.command()
async def rank_number(ctx, number_1, number_2):
    await ctx.send(int(number_1) ** int(number_2))

#Trash can

@bot.command()
async def trash(ctx):
    await ctx.send('Enter the trash name')
    msg = await bot.wait_for("message")
    if msg.content in trash_list_a:
        await ctx.send('Put it in the inorganic trash')
    elif msg.content in trash_list_o:
        await ctx.send('Put it in the organic trash')
    elif msg.content in trash_list_b:
        await ctx.send('Put it in the dangerous trash can')

#hehehe

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

#Token

bot.run("SECRET TOKEN")
