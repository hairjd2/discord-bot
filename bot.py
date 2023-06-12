import discord
import scorekeeper
from discord import option
import config

scoreboard = {}

def runBot():
    bot = discord.Bot()
    scoreboard = scorekeeper.initializeBoard()

# Add a player
    @bot.slash_command(name="addplayer", guild_ids=[490682611065421826, 670684341684142111])  # replace with your guild id
    @option(
        "name",
        str,
        description="Name of player you want to add"
    )
    async def addplayer(ctx, name):
        await ctx.respond(scorekeeper.addplayer(name, scoreboard))

# Delete a player
    @bot.slash_command(name="deleteplayer", guild_ids=[490682611065421826, 670684341684142111])  # replace with your guild id
    @option(
        "name",
        str,
        description="Name of player you want to delete"
    )
    async def deleteplayer(ctx, name):
        await ctx.respond(scorekeeper.deleteplayer(name, scoreboard))

# Get the score of a player
    @bot.slash_command(name="getscore", guild_ids=[490682611065421826, 670684341684142111])  # replace with your guild id
    @option(
        "name",
        str,
        description="Name of player you want to see the score of"
    )
    async def getscore(ctx, name):
        await ctx.respond(scorekeeper.getscore(name, scoreboard))

# Add one point to player name given
    @bot.slash_command(name="addone", guild_ids=[490682611065421826, 670684341684142111])  # replace with your guild id
    @option(
        "name",
        str,
        description="Name of player you want to increment the score of"
    )
    async def addone(ctx, name):
        await ctx.respond(scorekeeper.addone(name))

# Add given points to given player name
    @bot.slash_command(name="addpoints", guild_ids=[490682611065421826, 670684341684142111])  # replace with your guild id
    @option(
        "name",
        str,
        description="Name of player you want to add points to"
    )
    @option(
        "points",
        int,
        description="Amount of points to add"
    )
    async def addpoints(ctx, name, points):
        await ctx.respond(scorekeeper.addpoints(name, points))

# Show full scoreboard
    @bot.slash_command(name="showplayers", guild_ids=[490682611065421826, 670684341684142111])
    async def showplayers(ctx):
        await ctx.respond(scorekeeper.showplayers(scoreboard))

# Synchronize the json file with current running scoreboard
    @bot.slash_command(name="syncfile", guild_ids=[490682611065421826, 670684341684142111])
    async def syncfile(ctx):
        await ctx.respond(scorekeeper.syncfile(scoreboard))

# Prints out all commands and their descriptions
    @bot.slash_command(name="help", guild_ids=[490682611065421826, 670684341684142111])
    async def help(ctx):
        await ctx.respond(scorekeeper.help())

# Funny message haha
    @bot.slash_command(name="johnxina", guild_ids=[490682611065421826, 670684341684142111])
    async def johnxina(ctx):
        await ctx.respond(scorekeeper.johnxina())

    @bot.slash_command(name="test", guild_ids=[490682611065421826, 670684341684142111])  # replace with your guild id
    @option(
        "text",
        str,
        description="Enter some text"
    )
    async def test_command(ctx, text):
        await ctx.respond(f"You wrote: {text}")

# Just for me
    @bot.slash_command(name="reset", guild_ids=[490682611065421826])
    async def reset(ctx):
        await ctx.respond(scorekeeper.reset(scoreboard))

# Allows me to set score
    @bot.slash_command(name="setscore", guild_ids=[490682611065421826])  # replace with your guild id
    @option(
        "name",
        str,
        description="Name of player you are setting the score of"
    )
    @option(
        "score",
        str,
        description="Score"
    )
    async def setScore(ctx, name, score):
        await ctx.respond(scorekeeper.setScore(name, score, scoreboard))

    bot.run(config.TOKEN)
