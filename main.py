import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
import asyncio
from keep_alive import keep_alive 

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix="&")

#FOR ARAM STATS
@bot.command()
async def aram(ctx, *args):
  charname = "".join(args).lower()

  def filename(x):
    arampath = '/home/runner/lolbot/aram/'
    extension = '.txt'
    file = arampath + x + extension
    return file

  path = filename(charname)
  with open(path) as f:
    text = f.read()
    await ctx.channel.send(text)

#FOR NORMAL/RANKED STATS
@bot.command()
async def normal(ctx, *args):
  charname = "".join(args).lower()

  def filename(x):
    normalpath = '/home/runner/lolbot/normal/'
    extension = '.txt'
    file = normalpath + x + extension
    return file

  path = filename(charname)

  with open(path) as f:
    text = f.read()
    await ctx.channel.send(text)

keep_alive()

bot.run(DISCORD_TOKEN)