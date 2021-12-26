# Copyright (c) Shulkk, 2021.
import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
from discord.commands import slash_command

bot = commands.Bot(command_prefix = ".")

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

initial_extensions = ['cogs.src']

if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="Under Development"))
    print("Connected to Discord Gateway!")

bot.run(TOKEN)