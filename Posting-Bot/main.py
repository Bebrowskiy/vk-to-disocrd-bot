import disnake
from disnake.ext import commands
import os
import json
from utils.utils import load_config


config = load_config()
prefix = config.get("prefix")
token = config.get("token")


bot = commands.Bot(command_prefix=prefix, intents=disnake.Intents.all())


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


def load_cogs(bot):
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            bot.load_extension(f'cogs.{filename[:-3]}')


if __name__ == '__main__':
    load_cogs(bot)
    bot.run(token)
