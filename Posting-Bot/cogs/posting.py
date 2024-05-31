import disnake
import vk_api
from disnake.ext import commands
from utils.utils import load_config


class ExampleCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = load_config()
        self.vk_session = vk_api.VkApi(app_id=self.config.get("app_id"),
                                       token=self.config.get("vk_token"))
        self.vk = self.vk_session.get_api()

    @commands.slash_command(name='post', description="Publishes the latest post from the VK community page")
    async def posting(self, ctx):
        response = self.vk.wall.get(
            owner_id=self.config.get("group_id"), count=1)
        if response['items']:
            post = response['items'][0]
            post_id = post['id']
            if post_id:
                text = post['text']
                attachments = post.get('attachments')
                channel_id = int(self.config.get("channel_id"))
                guild = ctx.guild
                channel = disnake.utils.get(guild.channels, id=channel_id)

            if text:
                embed = disnake.Embed(
                    title=None,
                    description=f"{text}")

                if attachments:
                    for attachment in attachments:
                        if attachment['type'] == 'photo':
                            photo_url = attachment['photo']['sizes'][-1]['url']
                            embed.set_image(
                                url=photo_url
                            )
                else:
                    pass

                await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(ExampleCog(bot))
