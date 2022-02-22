import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='[')

@bot.event
async def on_ready():
    print(">> Bot is online <<")

@bot.event
async def on_member_join(member):
    print(f'{member} join!')
    channel = bot.get_channel(944443362608549938)
    await channel.send(f'{member} join!')

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(944443362608549938)
    await channel.send(f'{member} leave!')

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)}(ms)')

bot.run('OTQ0NDQ4ODE4NTEzMDYzOTU3.YhBwgQ.Jg9zqeT5Z-QplenWW11wFhf_bwo')
