import disnake
import vk_api
from disnake.ext import commands
from utils.utils import load_config


class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="ping", description="Check if the bot is online")
    async def ping(self, ctx):
        await ctx.send("Pong!")


def setup(bot):
    bot.add_cog(Ping(bot))
