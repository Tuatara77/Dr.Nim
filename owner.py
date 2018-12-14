import discord
from discord.ext import commands


class Owner:
    def __init__(self, bot):
        self.bot = bot

    async def __local_check(self, ctx):
        owner = await self.bot.is_owner(ctx.author)
        if owner is True:
            return True
        else:
            return False


    @commands.command()
    async def leave(self, ctx):
        await ctx.guild.leave()

def setup(bot):
    bot.add_cog(Owner(bot))