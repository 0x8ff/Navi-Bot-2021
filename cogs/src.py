from discord.ext import commands
from discord.commands import slash_command

class src(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(guild_ids=[936086088836079716], description='Navi Source Code')
    async def src(self, ctx):
        await ctx.respond("https://github.com/0x8FF/Navi")

def setup(bot):
    bot.add_cog(src(bot))