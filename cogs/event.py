from asyncio import events
from discord.ext import commands

import customFunc

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
        info = customFunc.botInfo()
        send = False
        for channel in guild.text_channels:
            if '天気予報' in channel.name and channel.permissions_for(guild.me).send_messages:
                await channel.send(embed=info)
                send = True
                break

        if send == False:
            for channel in guild.text_channels:
                if channel.permissions_for(guild.me).send_messages:
                    await channel.send(embed=info)
                    break


def setup(bot):
    bot.add_cog(event(bot))
