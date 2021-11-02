import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
from discord.commands import slash_command

bot = commands.Bot(command_prefix = ".")

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

bot.load_extension("cogs.src")

@bot.event
async def on_ready():
    print("Connected to Discord Gateway!")

bot.run(TOKEN)