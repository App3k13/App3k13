import discord
import pas_gen
import os
import random 

from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')


@bot.command()
async def hello(ctx):
    """ Bot się z tobą wita """
    await ctx.send(f'Hej!')

@bot.command()
async def bye(ctx):
    """ Bot się z tobą żegna """
    await ctx.send(f'Do widzenia!')

@bot.command()
async def meme(ctx):
    """ Bot wysyła mema"""
    all_images_in_folder = os.listdir('images')
    random_image = random.choice(all_images_in_folder)
    with open(f'images/{random_image}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

advices = ["Rób zakupy z materiałową torbą.", "Zamień wodę butelkowaną na wodę z kranu.","Kupuj kosmetyki naturalne w opakowaniach nadających się do recyklingu.","Kupuj produkty na wagę.","Nie drukuj, jeśli nie musisz, albo drukuj dwustronnie.","Wybieraj rachunki oraz faktury w wersji elektronicznej."]
@bot.command()
async def environmentadvice(ctx):
    """ Wybiera losową radę na temat środowiska """
    advice = random.choice(advices)
    await ctx.send(advice) 


bot.run("Token is here")
