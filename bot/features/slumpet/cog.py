from discord import Message
from discord.ext import commands
import logging
from re import compile, IGNORECASE

logger = logging.getLogger(__name__)


class SlumpetCog(commands.GroupCog, name="slumpet"):
    @commands.Cog.listener()
    async def on_message(self, message: Message):
        if message.author.bot:
            return False
        if message.channel.type == 1:  # Ignore DMs
            return False
        if "trumpet" not in message.content.lower():
            return False
        print("How many times")
        pattern = compile("trumpet", IGNORECASE)
        print(message.content)
        edited_message_text = pattern.sub("slumpet", message.content)
        print(edited_message_text)
        author = message.author.display_name
        attachments = [await f.to_file() for f in message.attachments]
        channel = message.channel
        await message.delete()

        await channel.send(content=f"**{author}:** {edited_message_text}", files=attachments)
        return False


async def setup(bot: commands.Bot):
    await bot.add_cog(SlumpetCog(bot))
