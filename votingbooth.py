import discord
from discord.ext import commands


class VotingBooth(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def ban(self, context):
        """Reaction set to vote on bans"""
        await context.message.add_reaction("🔨")
        await context.message.add_reaction("🇳")

    @commands.command(pass_context=True)
    async def vote(self, context):
        """Reaction set to vote on general voting matters."""
        await context.message.add_reaction("🇾")
        await context.message.add_reaction("🇳")

    @commands.command(pass_context=True)
    async def multi(self, context, multi_count):
        "currently not working, please do not use."
        for i in range(int(multi_count)):
            current_emoji = "3"
            print(current_emoji)
            await context.message.add_reaction(current_emoji)


def setup(bot):
    bot.add_cog(VotingBooth(bot))
