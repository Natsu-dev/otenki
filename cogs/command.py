from discord.ext import commands
import phrases

class command(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print('Inf: Class "command" is instantiated.')

    @commands.command()
    async def info(self, ctx):
        await ctx.send(embed=phrases.info)


def setup(bot):
    bot.add_cog(command(bot))
