import discord
from discord.ext import commands


class Help_Command:
    def __init__(self, bot):
        self.bot = bot

    @commands.group(invoke_without_command=True)
    async def help(self, ctx):
        em = discord.Embed(title='help', colour=0xc0ffee)
        em.add_field(name='note', value=";note <words>  |  Note stuff down and then Dr.Nim will DM the message you wanted to be noted down to you, making it easy to access.", inline=False)
        em.add_field(name="ping", value=";ping  |  Tells you the latency of the bot.", inline=False)
        em.add_field(name="serverinfo", value=";serverinfo  |  Shows you information about the server.", inline=False)
        em.add_field(name="userinfo", value=";userinfo <user> / <user id> (optional)  |  Shows you information about yourself, unless you either @mention someone or place their user id after the command.", inline=False)
        em.add_field(name="Help Modules", value="<moderator>", inline=False)
        await ctx.send(embed=em)

    @help.group()
    async def moderator(self, ctx):
        em = discord.Embed(title='help', colour=0xc0ffee)
        em.add_field(name="say", value=";say <words>  |  Make me say what you tell me to.", inline=False)
        em.add_field(name="purge", value=";purge <1-100>  |  Purge any amount of messages from 1 to 100.", inline=False)
        em.add_field(name="dm", value=";dm <user> / <user id>  |  Send that, then when I say 'please type your message now' then send another message with the text you want me to send that person. Once I have done it, I will send a message saying 'Your message has been sent'.", inline=False)
        em.add_field(name="addrole", value=";addrole <user> / <user id>  <role>  |  Add a role to a user", inline=False)
        em.add_field(name="remove role", value=";remrole <user> / <user id>  <role>  |  Remove a role from a user")
        await ctx.send(embed=em)

def setup(bot):
    bot.add_cog(Help_Command(bot))
