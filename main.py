import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
import asyncio
from keep_alive import keep_alive

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix="aery ")

@bot.event
async def on_ready():
  print('We have logged in as {0.user}'.format(bot))
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='aery info'))

#FOR ARAM STATS
@bot.command()
async def aram(ctx, *args):
  charname = "".join(args).lower().replace("'", "").replace(".", "")
  
  def filename(x):
    arampath = '/home/runner/Aerybot/aram/'
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
  charname = "".join(args).lower().replace("'", "").replace(".", "")
  
  def filename(x):
    normalpath = '/home/runner/Aerybot/normal/'
    extension = '.txt'
    file = normalpath + x + extension
    return file
    
  path = filename(charname)
  
  with open(path) as f:
    text = f.read()
    await ctx.channel.send(text)

@bot.command()
async def info(ctx):
	with open("info.txt") as f:
		text = f.read()
		await ctx.channel.send(text)


@bot.command()
async def comandos(ctx):
	with open("comandos.txt") as f:
		text = f.read()
		await ctx.channel.send(text)


@bot.command()
async def rotacion(ctx):
	with open("rotacion.txt") as f:
		text = f.read()
		await ctx.channel.send(
		    '**Los champs en rotación de esta semana son:** \n{}'.format(text))

@bot.command()
async def guilds(ctx):
  print(bot.guilds)

@bot.command()
async def replace(ctx):
  pruebas = ['prueba.txt', 'prueba2.txt']
  for i in pruebas:
    ori = open(i, 'r')
    new = ori.read()
    new = new.replace('haser', 'hacer').replace('parrafo', 'párrafo').replace('cip', 'sip')
    ori.close()
    ori = open(i, 'w')
    ori.write(new)
    ori.close()


keep_alive()

bot.run(DISCORD_TOKEN)