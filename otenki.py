# coding: UTF-8

# Packages
import discord
from discord.ext import commands
from discord.utils import find
import traceback  # show errors

# Custom Libraries
import loadenv


INITIAL_EXTENSIONS = [
    'cogs.event'
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
        print('ready...')


# Run
if __name__ == '__main__':
    bot = MyBot(command_prefix='>',
                # '<OS name> <version>をプレイ中'
                activity=discord.Game('気象庁(非公式)'))
    bot.run(loadenv.TOKEN)
