from asyncio.windows_events import NULL
from discord.ext import commands
import phrases
import customFunc
import sys

class command(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print('Inf: Class "command" is instantiated.')

    @commands.command()
    async def info(self, ctx):
        info = customFunc.botInfo()
        await ctx.send(embed=info)

    @commands.command()
    async def forecast(self, ctx, arg = ''):
        if arg.isdecimal():
            argInt = int(arg)
        else:
            argInt = -1
        
        if argInt >= 0 and argInt <= 6:
            forecast = customFunc.forecast(argInt)
        else:
            forecast = customFunc.forecast()

        await ctx.send(embed=forecast)


def setup(bot):
    bot.add_cog(command(bot))
