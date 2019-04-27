import discord
from asyncio import gather
from discord.ext import commands
import os

bot = commands.Bot(
    command_prefix="!", description="Bot to help /r/kpop do things"
)

if __name__ == "__main__":
    bot.load_extension("votingbooth")
    bot.run(os.getenv("TOKEN"))

