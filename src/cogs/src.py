from discord.ext import commands
from discord.commands import slash_command

class src(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(description='Umi Source Code')
    async def src(self, ctx):
        await ctx.respond("https://github.com/x86guy/umi.py")

def setup(bot):
    bot.add_cog(src(bot))