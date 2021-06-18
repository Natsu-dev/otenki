# coding: UTF-8

import urllib.request as req
import discord
from discord.ext import tasks, commands
import datetime
import json

class periodic(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.minloop.start()
        print('Inf: Class "periodic" is instantiated.')

    @tasks.loop(seconds=60)
    async def minloop(self):
        #if datetime.datetime.now().strftime('%H-%M') == '22-00':

            #週間天気予報のjsonを取ってくる
            #url = 'https://www.jma.go.jp/bosai/forecast/data/forecast/010000.json'
            #filename = 'tenki.json'
            #req.urlretrieve(url, filename)

            for guild in self.bot.guilds:
                for channel in guild.text_channels:
                    if channel.permissions_for(guild.me).send_messages:
                        await channel.send('時報')
                        break

def setup(bot):
    bot.add_cog(periodic(bot))
