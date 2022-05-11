# IMPORT
import discord
import os
import requests
import json.decoder
from dotenv import load_dotenv
from discord.ext import tasks
from discord.ext import commands

# LOADS THE .ENV FILE THAT RESIDES ON THE SAME LEVEL AS THE SCRIPT.
load_dotenv()

# GRAB THE API TOKEN FROM THE .ENV FILE.
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

zib_counter = 0


# GETS THE CLIENT OBJECT FROM DISCORD.PY. CLIENT IS SYNONYMOUS WITH BOT.
bot = discord.Client()

# EVENT LISTENER FOR WHEN THE BOT HAS SWITCHED FROM OFFLINE TO ONLINE.
@bot.event
async def on_ready():
	# CREATES A COUNTER TO KEEP TRACK OF HOW MANY GUILDS / SERVERS THE BOT IS CONNECTED TO.
	guild_count = 0

	# LOOPS THROUGH ALL THE GUILD / SERVERS THAT THE BOT IS ASSOCIATED WITH.
	for guild in bot.guilds:
		# PRINT THE SERVER'S ID AND NAME.
		print(f"- {guild.id} (name: {guild.name})")

		# INCREMENTS THE GUILD COUNTER.
		guild_count = guild_count + 1

	# PRINTS HOW MANY GUILDS / SERVERS THE BOT IS IN.
	print("SampleDiscordBot is in " + str(guild_count) + " guilds.")
	send_kanye_quote.start(discord.utils.get(bot.get_all_channels(), name="general"))

# EVENT LISTENER FOR WHEN A NEW MESSAGE IS SENT TO A CHANNEL.
@bot.event
async def on_message(message):
	global zib_counter

	# CHECKS IF THE MESSAGE THAT WAS SENT IS EQUAL TO "HELLO".
	if message.content == "saf":
		# SENDS BACK A MESSAGE TO THE CHANNEL.
		zib_counter += 1
		await message.channel.send(f" zib + {zib_counter}")
	if message.content =="sterk":
		zib_counter += 1
		await message.channel.send(f" zib + {zib_counter}")
		# await message.channel.send(" zib + {}").format(zib_counter)

def get_kayne_tweet():
	kayne_tweet = requests.get("https://api.kanye.rest/").json()
	return kayne_tweet['quote']

@tasks.loop(seconds=5)
async def send_kanye_quote(channel):
	await channel.send(get_kayne_tweet())



# EXECUTES THE BOT WITH THE SPECIFIED TOKEN. TOKEN HAS BEEN REMOVED AND USED JUST AS AN EXAMPLE.
bot.run(DISCORD_TOKEN)