import discord
from discord.ext import commands

# try :
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def smile(ctx):
    await ctx.send(f':D')

@bot.command()
async def cry(ctx):
    await ctx.send(f':_(')

@bot.command()
async def plus(ctx, letter_1, letter_2):
    await ctx.send(int(letter_1) + int(letter_2))

@bot.command()
async def multiply(ctx, number_1, number_2):
    await ctx.send(int(number_1) * int(number_2))

@bot.command()
async def rank_number(ctx, number_1, number_2):
    await ctx.send(int(number_1) ** int(number_2))

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

bot.run("SECRET TOKEN HERE")
