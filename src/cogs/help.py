from discord.ext import commands
from discord.commands import slash_command

class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(guild_ids=[903901767920680972], description='Help Command')
    async def help(self, ctx):
        await ctx.respond("WORK IN PROGRESS")

def setup(bot):
    bot.add_cog(help(bot))