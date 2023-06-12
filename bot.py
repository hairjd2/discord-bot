import discord
import scorekeeper
from discord.ext import commands
import config

def runBot():
    client = discord.Client(intents=discord.Intents.default())

    intents = discord.Intents.default()
    intents.members = True
    intents.typing = True
    intents.presences = True
    intents.message_content = True
    client = commands.Bot(command_prefix="/", intents=intents)

    @client.event
    async def on_ready():
        print("Bot is online")

    # responses.checkCommand(client)

    @client.command()
    async def ping(ctx):
        await ctx.send("Pong!")

    @client.command()
    async def test(ctx):
        await ctx.send("test worked!")

    @client.command('addone')
    async def addone(ctx, *, name):
        await ctx.send("test worked!")
 
    client.run(config.TOKEN)
