import discord
from discord.ext import commands

class Mod:
    def __init__(self, bot):
        self.bot = bot

    async def __local_check(self, ctx):
        guild = ctx.guild
        role1 = discord.utils.get(guild.roles, id=451412255129468939)
        role2 = discord.utils.get(guild.roles, id=506132822927474704)
        role3 = discord.utils.get(guild.roles, id=508636962903818251)
        role4 = discord.utils.get(guild.roles, id=510818827110711296)
        role5 = discord.utils.get(guild.roles, id=466066309088804866)
        if role1 in ctx.author.roles or role2 in ctx.author.roles or role3 in ctx.author.roles or role4 in ctx.author.roles:
            return True
        else:
            return False

    @commands.command()
    async def say(self, ctx, *, words):
        await ctx.message.delete()
        await ctx.send(f"{words}")

    @commands.command()
    async def purge(self, ctx, amount: int = None):
        if amount is None:
            await ctx.channel.purge(limit=2)
            await ctx.send(f"1 message deleted", delete_after=5)
        elif amount > 100:
            await ctx.send(f"the limit of messages I can delete at one time is 100.", delete_after=5)
        else:
           clear = amount + 1
           await ctx.channel.purge(limit=clear)
           await ctx.send(f"{amount} messages deleted", delete_after=5)

    @commands.command()
    async def dm(self, ctx, user: discord.Member = None):
        if user is None:
            await ctx.send("Please insert the name of a user you want me to dm.")
        else:
            await ctx.send("Please type your message now")
            def check(m):
                return m.author == ctx.author
            try:
                msg = await self.bot.wait_for('message', check=check)
                words = msg.content
                await user.send(words)
            finally:
                await ctx.send("Your message has been sent")

    async def on_message(self, message):
        in_dm = message.guild is None
        is_not_from_me = message.author != self.bot.user
        channel = discord.utils.get(self.bot.get_all_channels(), guild__name="The Tuatara Lodge", name='dms-sent-to-nim')
        if in_dm and is_not_from_me:
            await channel.send(f'{message.author.mention} ')
            await channel.send(message.content)

def setup(bot):
    bot.add_cog(Mod(bot))
