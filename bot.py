import discord
import logging
import os
from discord.ext import commands

logging.basicConfig(level='INFO')
logger = logging.getLogger('Logs')

bot = commands.Bot(description=' ', command_prefix=commands.when_mentioned_or(";"), pm_help=False)

setattr(bot, "logger", logger)

@bot.event
async def on_ready():
    print("On standby, Master")
    await bot.change_presence(activity=discord.Game(name="being programmed by Tuatara_77"))

@bot.command()
async def say(ctx, *, words):
    await ctx.message.delete()
    await ctx.send(f"{words}")

@bot.command()
async def userinfo(ctx, member: discord.Member=None):
    if member is None:
        member = ctx.author
        display = member.name
        discrim = member.discriminator
        name = f'{display}#{discrim}'
        joindate = f'{member.joined_at.day}-{member.joined_at.month}-{member.joined_at.year}'
        joined = f'{joindate}, {str(member.joined_at.time())[:-10]}'
        createddate = f'{member.created_at.day}-{member.created_at.month}-{member.created_at.year}'
        created = f'{createddate}, {str(member.created_at.time())[:-10]}'
        em = discord.Embed(title='Userinfo', colour=0xc0ffee)
        em.set_thumbnail(url=member.avatar_url)
        em.add_field(name='Name:', value=name, inline=False)
        em.add_field(name='Nickname:', value=member.nick, inline=False)
        em.add_field(name='User id', value=member.id, inline=False)
        em.add_field(name='Status', value=member.status, inline=False)
        em.add_field(name='Created at:', value=created, inline=False)
        em.add_field(name='Joined at:', value=joined, inline=False)
        em.add_field(name='Roles:', value=','.join(r.name if r.name == '@everyone' else r.mention for r in sorted(member.roles, key=str)), inline=False)
        await ctx.send(embed=em)
    else:
        display = member.name
        discrim = member.discriminator
        name = f'{display}#{discrim}'
        joindate = f'{member.joined_at.day}-{member.joined_at.month}-{member.joined_at.year}'
        joined = f'{joindate}, {str(member.joined_at.time())[:-10]}'
        createddate = f'{member.created_at.day}-{member.created_at.month}-{member.created_at.year}'
        created = f'{createddate}, {str(member.created_at.time())[:-10]}'
        em = discord.Embed(title='Userinfo', colour=0xc0ffee)
        em.set_thumbnail(url=member.avatar_url)
        em.add_field(name='Name:', value=name, inline=False)
        em.add_field(name='Nickname:', value=member.nick, inline=False)
        em.add_field(name='User id', value=member.id, inline=False)
        em.add_field(name='Status', value=member.status, inline=False)
        em.add_field(name='Created at:', value=created, inline=False)
        em.add_field(name='Joined at:', value=joined, inline=False)
        em.add_field(name='Roles:', value=','.join(r.name if r.name == '@everyone' else r.mention for r in sorted(member.roles, key=str)), inline=False)
        await ctx.send(embed=em)

bot.run(os.environ['TOKEN'])
