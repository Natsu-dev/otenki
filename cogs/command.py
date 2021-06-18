from discord.ext import commands
import phrases
import customFunc

class command(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print('Inf: Class "command" is instantiated.')

    @commands.command()
    async def info(self, ctx):
        await ctx.send(embed=phrases.info)

    @commands.command()
    async def forecast(self, ctx):
        forecast = customFunc.tomorrowForecast()
        await ctx.send(embed=forecast)


def setup(bot):
    bot.add_cog(command(bot))
