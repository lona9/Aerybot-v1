import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
import asyncio
from keep_alive import keep_alive

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix="aery ")

## STATUS = ALL FILES UP TO DATE, NAMES REPLACED.
## REPLACE LIST NEEDS UPDATING

@bot.event
async def on_ready():
  print('We have logged in as {0.user}'.format(bot))
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='aery info'))

@bot.event
async def on_guild_join(guild):
  lona = await bot.fetch_user(485054727755792410)
  await lona.send('aery se unió a {} ({} miembros)'.format(guild.name, guild.member_count))

@bot.event
async def on_guild_remove(guild):
  lona = await bot.fetch_user(485054727755792410)
  await lona.send('aery fue expulsada de {} ({} miembros)'.format(guild.name, guild.member_count))

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
  if os.path.exists(path):
    with open(path) as f:
      text = f.read()
      await ctx.channel.send(text)
    print(str(ctx.message.content), ctx.guild)
  else:
    await ctx.channel.send("¡No existe ese archivo! ¿Escribiste bien el nombre?\nLa forma correcta de escribir el comando es *aery aram champ*, usa el nombre completo, sin importar mayúsculas ni carácteres especiales (Ej: Se puede escribir *aery aram Cho'Gath* o *aery aram chogath*, *aery aram Lee Sin* o *aery aram leesin* or incluso *aery aram LeEsIn*, se debe buscar *aery aram Nunu y Willump*, y no solo *aery aram Nunu*)")


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

  if os.path.exists(path):
    with open(path) as f:
      text = f.read()
      await ctx.channel.send(text)
    print(str(ctx.message.content), ctx.guild)
  else:
    await ctx.channel.send("¡No existe ese archivo! ¿Escribiste bien el nombre?\nLa forma correcta de escribir el comando es *aery normal champ*, usa el nombre completo, sin importar mayúsculas ni carácteres especiales (Ej: Se puede escribir *aery normal Cho'Gath* o *aery normal chogath*, *aery normal Lee Sin* o *aery normal leesin* or incluso *aery normal LeEsIn*, se debe buscar *aery normal Nunu y Willump*, y no solo *aery normal Nunu*)")


@bot.command()
async def info(ctx):
  print(str(ctx.message.content), ctx.guild)
  with open("info.txt") as f:
    text = f.read()
    await ctx.channel.send(text)

@bot.command()
async def comandos(ctx):
  print(str(ctx.message.content), ctx.guild)
  with open("comandos.txt") as f:
    text = f.read()
    await ctx.channel.send(text)


@bot.command()
async def rotacion(ctx):
  print(str(ctx.message.content), ctx.guild)
  with open("rotacion.txt") as f:
    text = f.read()
    await ctx.channel.send(
		    '**Los champs en rotación de esta semana son:** \n{}'.format(text))

@bot.command()
async def comentario(ctx):
  lona = await bot.fetch_user(485054727755792410)
  await lona.send('{} dice: {}'.format(ctx.message.author, ctx.message.content))

@bot.command()
async def guilds(ctx):
  print(bot.guilds)

keep_alive()

bot.run(DISCORD_TOKEN)