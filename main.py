import discord 
import os
from dotenv import load_dotenv
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

bot = discord.Client()

@bot.event
async def on_ready():
    print("Server started")


#bot.run(DISCORD_TOKEN)

import discord_commands