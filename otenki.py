# coding: UTF-8

# Packages
import discord
from discord.ext import commands
import traceback  # show errors

# Custom Libraries
import loadenv
import phrases

VERSION = '0.0.1'

INITIAL_EXTENSIONS = [
    'cogs.event',
    'cogs.command',
    'cogs.periodic'
]


class MyBot(commands.Bot):

    def __init__(self, command_prefix, activity):

        super().__init__(command_prefix, activity=activity)

        for cog in INITIAL_EXTENSIONS:
            try:
                self.load_extension(cog)
            except Exception:
                traceback.print_exc()

    async def on_ready(self):
        print('USER: ' + self.user.name)
        print('ID: ' + str(self.user.id))

        print('Servers:')
        for guild in bot.guilds:
            print(guild.name)

        print('ready...')


# Run
if __name__ == '__main__':
    bot = MyBot(command_prefix='t:',
        # 't:infoをプレイ中'
        activity=discord.Game(phrases.activity))
    bot.run(loadenv.TOKEN)
