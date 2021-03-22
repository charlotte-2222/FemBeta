import random
from datetime import datetime

import aiohttp
import discord
from discord.ext import commands


class FunCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def insult(self, ctx):
        """random insult"""
        lines = open('text_dir/insults.txt').read().splitlines()
        await ctx.send(random.choice(lines))
        await ctx.message.delete()

    @commands.command(aliases=["dick", "penis"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def dong(self, ctx, *, user: discord.Member):
        """Detects user's dong length"""
        state = random.getstate()
        random.seed(user.id)
        dong = "8{}D".format("=" * random.randint(0, 30))
        random.setstate(state)
        em = discord.Embed(title="{}'s Dong Size".format(user), description="Size: " + dong,
                           colour=discord.Colour.magenta())
        await ctx.send(embed=em)

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def daddy(self, ctx):
        author = ctx.author
        async with aiohttp.ClientSession() as session:
            async with session.get("https://dadjoke-api.herokuapp.com/api/v1/dadjoke") as r:
                data = await r.json()
                d = discord.Embed(title=f":milk: Hey, I found the milk", description=data['joke'],
                                  color=discord.Color.magenta()
                                  , timestamp=datetime.utcnow())
                await ctx.send(embed=d)

    @daddy.error
    async def daddy_error(ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title="Dad jokes are temporary, just like your actual dad",
                               color=discord.Color.magenta())
            await ctx.send(embed=em)


def setup(bot):
    bot.add_cog(FunCog(bot))
