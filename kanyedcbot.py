# IMPORT
import discord
import os
import requests
import json.decoder
from dotenv import load_dotenv
from discord.ext import tasks
from discord.ext import commands


load_dotenv()


DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

zib_counter = 0



bot = discord.Client()


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

@tasks.loop(seconds=5)
async def send_kanye_quote(channel):
	await channel.send(get_kayne_tweet())


bot.run(DISCORD_TOKEN)
