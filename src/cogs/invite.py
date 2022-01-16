from discord.ext import commands
from discord.commands import slash_command

class invite(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(guild_ids=[932084005707337788], description='Server Invite Link')
    async def invite(self, ctx):
        await ctx.respond("https://discord.gg/XAuZHkwZ7N")

def setup(bot):
    bot.add_cog(invite(bot))