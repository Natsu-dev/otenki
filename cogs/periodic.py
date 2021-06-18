# coding: UTF-8

import urllib.request as req
import discord
from discord.ext import tasks, commands
import datetime
import customFunc

class periodic(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.minloop.start()
        print('Inf: Class "periodic" is instantiated.')

    @tasks.loop(seconds=60)
    async def minloop(self):
        if datetime.datetime.now().strftime('%H-%M') == '22-00':

            forecast = customFunc.forecast(1)

            for guild in self.bot.guilds:
                send = False
                for channel in guild.text_channels:
                    if '天気予報' in channel.name and channel.permissions_for(guild.me).send_messages:
                        await channel.send(embed=forecast)
                        send = True
                        break

                if send == False:
                    for channel in guild.text_channels:
                        if channel.permissions_for(guild.me).send_messages:
                            await channel.send(embed=forecast)
                            break


def setup(bot):
    bot.add_cog(periodic(bot))
