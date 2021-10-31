import discord
from discord.ext import commands
from discord.commands import slash_command

bot = commands.Bot(command_prefix = ".")

@bot.event
async def on_ready():
    print("Connected to Discord Gateway!")

@bot.slash_command(guild_ids = [903901767920680972])
async def ping(ctx):
    await ctx.respond("Pong!")

bot.run("DISCORD_BOT_TOKEN")