import discord
import pas_gen

from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')

@bot.command()
async def joined(ctx, member: discord.Member):
    await ctx.send(f'{member.name} dołączył {discord.utils.format_dt(member.joined_at)}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Cześć!')

@bot.command()
async def bye(ctx):
    await ctx.send(f'Do zobaczenia!')

@bot.command()
async def goodmorning(ctx):
    await ctx.send(f'Dzień dobry!')   


bot.run("Token is here")
