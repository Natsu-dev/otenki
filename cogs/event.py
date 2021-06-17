from asyncio import events
from discord.ext import tasks, commands

class event(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print('Inf: Class "event" is instantiated.')

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        # Good Morning
        if 'test' in message.content:
            await message.channel.send('test')
            print('sent test message.')
            return

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        for channel in guild.text_channels:
            if channel.permissions_for(guild.me).send_messages:
                await channel.send('Joined {}!'.format(guild.name))
                break


def setup(bot):
    bot.add_cog(event(bot))
