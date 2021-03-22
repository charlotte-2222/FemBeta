from datetime import datetime

import discord
from discord.ext import commands


class OwnerCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def maintenance(self, ctx):
        linkEmbed = discord.Embed(title='FemboyBot is going down... not in that way...', timestamp=datetime.utcnow())
        linkEmbed.set_image(url='https://i.imgur.com/7G5vvvt.png')
        linkEmbed.add_field(name="What should I do while I'm waiting?",
                            value="Play a game\nlookup futa & feet elsewhere\nmaybe message flop for status.")
        linkEmbed.color = discord.Color.from_rgb(239, 124, 243)
        await ctx.send(embed=linkEmbed)
        await ctx.message.delete()



def setup(bot):
    bot.add_cog(OwnerCog(bot))
