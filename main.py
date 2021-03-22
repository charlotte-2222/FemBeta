import discord
from discord.ext import commands

import sys, traceback
import asyncio
from datetime import time
from config import token

def get_prefix(bot, message):
    prefixes=['>>']

    if not message.guild:
        return'?'
    return commands.when_mentioned_or(*prefixes)(bot, message)

initial_extensions = ['cogs.admin',
                      'cogs.fun',
                      'cogs.hentai',
                      'cogs.owner',
                      'cogs.reddit',
                      'cogs.redditNSFW']
bot=commands.Bot(command_prefix=get_prefix, description='Using Eviees cog rewrite')

if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)

@bot.event
async def on_ready():
    print("FemBot online")
    print("--------------")
    print(time.strftime("Time at start:\n" + "%H:%M:%S\n" +
                        "%m/%d/%Y\n"
                        f"\nLogged in as {bot.user.name} - {bot.user.id}\n"
                        f"{discord.__version__}\n"))

    while True:
        await bot.change_presence(
            activity=discord.Activity(type=discord.ActivityType.watching, name="For ^ | ^help"))
        await asyncio.sleep(20)
        await bot.change_presence(status=discord.Status.online, activity=discord.Game('with The Fragment'))
        await asyncio.sleep(20)
        await bot.change_presence(
            activity=discord.Activity(type=discord.ActivityType.streaming, name="Futa Fix 2"))
        await asyncio.sleep(20)
        await bot.change_presence(
            activity=discord.Activity(type=discord.ActivityType.watching, name="For ^ | ^help"))
        await asyncio.sleep(20)
        await bot.change_presence(
            activity=discord.Activity(type=discord.ActivityType.listening, name='heavy moans'))
        await asyncio.sleep(20)
        await bot.change_presence(status=discord.Status.dnd, activity=discord.Game('Destiny 2 (Naked)'))
        await asyncio.sleep(20)
        await bot.change_presence(
            activity=discord.Activity(type=discord.ActivityType.watching, name="For ^ | ^help"))
        await asyncio.sleep(20)
        await bot.change_presence(status=discord.Status.idle, activity=discord.Game('Halo 3'))
        await asyncio.sleep(20)
        await bot.change_presence(status=discord.Status.dnd, activity=discord.Game('with all the Homies'))
        await asyncio.sleep(20)
        await bot.change_presence(
            activity=discord.Activity(type=discord.ActivityType.watching, name="For ^ | ^help"))
        await asyncio.sleep(20)


bot.run(token, bot=True, reconnect=True)