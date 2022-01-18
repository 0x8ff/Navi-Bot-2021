from discord.ext import commands
from discord.commands import slash_command

class src(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(guild_ids=[932084005707337788], description='Miku Source Codex')
    async def src(self, ctx):
        await ctx.respond("https://github.com/0x8FF/MikuBot")

def setup(bot):
    bot.add_cog(src(bot))