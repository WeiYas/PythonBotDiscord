import discord 
import os

from dotenv import load_dotenv
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

from discord.ext import commands
commandbot = commands.Bot(command_prefix = '$')

@commandbot.command()
async def info(message) :
    await message.send(f'Servername: {message.guild}')

@commandbot.command()
async def piti(message) :
    await message.send('Meowy hellow for <@178897090573762561>')

@commandbot.command()
async def sgf(message) :
    await message.send('https://media.discordapp.net/attachments/860234327852711946/969912265182674944/unknown.png')

@commandbot.command()
async def dozi(message) :
    await message.send('<:crownLama:969917561007386654>')
    await message.send('<:Dozi:969914649086660689>')
    await message.send('<:YoshiBike:969914599178666054>')


commandbot.run(DISCORD_TOKEN)