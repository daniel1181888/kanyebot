# IMPORT
from pydoc import describe
from turtle import color, title
import discord
import os
import requests
import json.decoder
from dotenv import load_dotenv
from discord.ext import tasks
from discord.ext import commands


load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
bot = discord.Client()

zib_counter = 0
i = 0
kanye_faces = [
  "https://dazedimg-dazedgroup.netdna-ssl.com/900/azure/dazed-prod/1150/9/1159008.jpg",
  "https://images0.persgroep.net/rcs/ZCVaR991An92JzBcUHrvHMc3jOc/diocontent/208811431/_fitwidth/694/?appId=21791a8992982cd8da851550a453bd7f&quality=0.8",
  "https://img.nieuwsblad.be/LJkYssWjIYWbhAyVlSvqAXL8QfY=/960x640/smart/https%3A%2F%2Fstatic.nieuwsblad.be%2FAssets%2FImages_Upload%2F2021%2F10%2F18%2Fb3607598-2407-4e40-8197-9db0dd86ca5d.jpg",
  "https://images.squarespace-cdn.com/content/v1/56983f4089a60aae9b0db521/1453926588347-CFTFLKGLP493ESFZ5Y3L/image-asset.jpeg?format=1000w",
  "https://www.toledoblade.com/image/2009/09/14/600x_q90_a4-3_cTCjpg/Kanye-West-Taylor-Swift.jpg"
]


@bot.event
async def on_ready():
	send_kanye_quote.start(discord.utils.get(bot.get_all_channels(), name="general"))


@bot.event
async def on_message(message):
	global zib_counter

	
	if message.content == "saf":
		
		zib_counter += 1
		await message.channel.send(f" zib + {zib_counter}")
	if message.content =="sterk":
		zib_counter += 1
		await message.channel.send(f" zib + {zib_counter}")
		

def get_kayne_tweet():
	kayne_tweet = requests.get("https://api.kanye.rest/").json()
	return kayne_tweet['quote']

@tasks.loop(hours=15)
async def send_kanye_quote(channel):
	await channel.send(embed=displayembed())


def displayembed():
	global i

	if i > len(kanye_faces) - 1:
		i = 0

	embed = discord.Embed(
		title = 'kanye quote',
		description = get_kayne_tweet(),
		color = discord.Color.red()
	)

	embed.set_image(url=kanye_faces[i])
	

	i += 1
	return embed


bot.run(DISCORD_TOKEN)
