import discord
import json
from discord.ext import commands

client = commands.Bot(command_prefix=";",intents=discord.Intents.all())


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game(';help for a list of commands !!!'))
    print('Boot successful')

@client.command()
async def ping(ctx):
    await ctx.send("Pong !")

@client.command()
async def lunanetwork(ctx):
    await ctx.send("<:lunanetwork:981940613069017138> https://sites.google.com/view/lunanetwork <:lunanetwork:981940613069017138>")

@client.command()
async def lunahub(ctx):
    await ctx.send("<:lunahub:981940577748795473> **Here are all of the domains for Luna Hub** | https://www.lunahub.gq |"
    " https://www.yousmellikefish.ml/ | https://sites.google.com/view/lunahub <:lunahub:981940577748795473>")

client.run("TOKEN")
