from discord.ext import commands
from discord.commands import slash_command

class avatar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(guild_ids=[932084005707337788], description='Get a users avatar ')
    async def invite(self, ctx):
        await ctx.respond("Lol")

def setup(bot):
    bot.add_cog(avatar(bot))