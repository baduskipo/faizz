import discord
from discord.ext import commands
# step 1
import os, random
from bot_iogic import sampah_anorganik, sampah_organik, greetings

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

# greet atau greet
@bot.command()
async def greet(ctx):
    await ctx.send(greetings)

    # organik
@bot.command()
async def organik(ctx):
    await ctx.send(sampah_organik)

# bikin perintah untuk sampah anorganik
@bot.command()
async def anorganik(ctx):
    await ctx.send(sampah_anorganik)
