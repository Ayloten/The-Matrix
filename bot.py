# imports

import discord
from discord.ext import commands
from pornhub_api import PornhubApi
from discord.utils import get
import json
import asyncio
import shutil
import requests
import os
import random
import time
import re


# prefix

client = commands.Bot(command_prefix = ",,")

# cogs for 8ball

@client.command()
async def load(ctx, extension):
	client.load_extension(f"cogs.{extension}")

@client.command()
async def unload(ctx, extension):
	client.unload_extension(f"cogs.{extension}")

for filename in os.listdir('./cogs'):
	if filename.endswith('.py'):
		client.load_extension(f'cogs.{filename[:-3]}')

#basic bot stuff and clear stuff too

@client.event
async def on_ready():
	print('Bot is ready.')

@client.event
async def on_guild_join(guild):
	general = find(lambda x: x.name == 'general',  guild.text_channels)
	if general and general.permissions_for(guild.me).send_messages:
		await general.send("Hello! I'm The Matrix Discord bot. my prefix is ',,', but you can't change it lmao. you may find i have created a role called 'Muted' and that is because i rely on that to mute people. you can however edit the role to your specifications and i will still mute people, as long as the name isnt changed. lmao enjoy ")

@client.event
async def on_member_join(member, ctx):
	await ctx.send(f'{member} has joined a server. LEAVE WHILE YOU STILL CAN')

@client.event
async def on_member_remove(member, ctx):
	await ctx.send(f'{member} has made the right choice.')


@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=5):
	await ctx.channel.purge(limit=amount)

@client.event
async def on_member_join(member):
	await member.send("Hey, Thanks for joining!")

# moderation

@client.event
async def on_message(message):
	if message.author.bot:
		return
	if "hello there" in message.content.lower():
		await message.channel.send("GENERAL KENOBI")
	if "fag" in message.content.lower():
		await message.delete()
		await message.channel.send("Swearing is allowed, just dont make it overkill.")
	if "faggot" in message.content.lower():
		await message.delete()
		await message.channel.send("Swearing is allowed, just dont make it overkill.")
	if "nigga" in message.content.lower():
		await message.delete()
		await message.channel.send("Swearing is allowed, just dont make it overkill.")
	if "nigger" in message.content.lower():
		await message.delete()
		await message.channel.send("Swearing is allowed, just dont make it overkill.")
	if "cunt" in message.content.lower():
		await message.delete()
		await message.channel.send("Swearing is allowed, just dont make it overkill.")
	if "fucking nigger" in message.content.lower():
		await message.delete()
		await message.channel.send("Swearing is allowed, just dont make it overkill.")
	if " heck" in message.content.lower():
		await message.channel.send("Please no saying heck or frick good sir this is a christian discord server establismemt.")
	if "frick" in message.content.lower():
		await message.channel.send("Please no saying heck or frick good sir this is a christian discord server establismemt.")
	if "yaaa" in message.content.lower():
		await message.channel.send ("It's rewind time!")
	if "shut up" in message.content.lower():
		await message.channel.send ("https://i.kym-cdn.com/photos/images/newsfeed/001/591/186/ab1.jpg")
	if "testword" in message.content.lower():
		await message.delete()
		await message.channel.send("Swearing is allowed, just dont make it overkill.")
	if "creeper" in message.content.lower():
		await message.channel.send("awwww man!")
	await client.process_commands(message)

#lists (dont delete as they make the random commnnds work)

coinflip = [
			'Heads!',
			'Tails!',
			'it landed sideways wtf',
]

randomnumbers = [
				 '1',
				 '2',
				 '3',
				 '4',
				 '5',
				 '6',
				 '7',
				 '8',
				 '9',
				 '10',
]
puns = [
		"Light travels faster than sound. That's why some people appear bright until you hear them speak",
		"I was wondering why the ball was getting bigger. Then it hit me",
		"I have a few jokes about unemployed people, but none of them work",
		"I have a split personality, said Tom, being frank.",
		"How do you make holy water? You boil the hell out of it",
		"I Renamed my iPod The Titanic, so when I plug it in, it says “The Titanic is syncing.”",
		"When life gives you melons, you're dyslexic",
		"Will glass coffins be a success? Remains to be seen",
		"Last night, I dreamed I was swimming in an ocean of orange soda. But it was just a Fanta sea",
		"I lost my job at the bank on my very first day. A woman asked me to check her balance, so I pushed her over (insert ba dum CRASH here)",
		"'Is this the real life? is this just fanta sea?' 'no freddie, its FANTASY. Have you been doing your speech impediment work?''",
		"What’s the difference between a hippo and a zippo? One is really heavy and the other is a little lighter",
		"Two windmills are standing in a wind farm. One asks, “What’s your favorite kind of music?” The other says, “I’m a big metal fan.”",
		"Did you hear about the guy whose whole left side was cut off? He’s all right now",
]

lennyfaces = [
			  "( ͡° ͜ʖ ͡°)",
			  "( ͡° ͜ʖ ͡°)╭∩╮",
			  "( • )( • )ԅ(≖⌣≖ԅ)",
			  "(‿!‿) ԅ(≖‿≖ԅ)",
			  "•́ε•̀٥",
			  "(͠≖ ͜ʖ͠≖)ε｀●)",
			  "( ㅅ )",
			  "͡° ͜ʖ ͡ –",
			  "ᕤ( ͡~ ͜ʖ ͡°)",
			  "( ͠° ͟ʖ ͡°)",
			  "( ͡~ ͜ʖ ͡°)",
			  "( ° ͜ʖ °)",
			  "( ͡ᵔ ͜ʖ ͡ᵔ )",
			  "(╯ ͠° ͟ʖ ͡°)╯┻━┻",
			  "｡*ﾟ.*.｡(っ ᐛ )っ✂╰⋃╯",
			  "( ͡ʘ ͜ʖ ͡ʘ)",
			  "( ͡o ͜ʖ ͡o)",
			  "( ಠ ͜ʖಠ)",
			  "(ง ͡ʘ ͜ʖ ͡ʘ)ง",
]

#banning and stuff

@client.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx, member: discord.Member , *, reason=None):
	await ctx.send(f"{member.mention} has been kicked from {ctx.guild.name}. ")
	if reason is None:
		reason = f"Kicked by {ctx.author.name}"

	#remove the "#" below if you also want to dm the user who is kicked
	await member.send(f"You Have Been Kicked from {ctx.guild.name} . Reason = {reason}")

	#if no reason is provided then the reason will be kicked by <name of the person who kicked>
	await member.kick(reason = reason)

@client.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member: discord.Member, *, reason=None):
	await ctx.send(f"{member.mention} has been banned from {ctx.guild.name}")
	if reason is None:
		reason = f"Banned by {ctx.author.name}"


	#remove the "#" below if you also want to dm the user that he is banned from the server
	await member.send(f"You Have Been Banned from {ctx.guild.name}. Reason: {reason}")

	#if no reason is provided then the reason will be banned by <the person who bans>
	await member.ban(reason = reason)

@client.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
	banned_users = await ctx.guild.bans()
	member_name, member_discriminator = member.split('#')

	for ban_entry in banned_users:
		user = ban_entry.user

		if (user.name, user.discriminator) == (member_name, member_discriminator):
			await ctx.guild.unban(user)
			await ctx.send(f'Unbanned {user.mention}')
			return

@client.command()
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member : discord.Member):
	guild = ctx.guild

	for role in guild.roles:
		if role.name == "Muted":
			await member.remove_roles(role)
			await ctx.send("{} has been unmuted by {} lol" .format(member.mention,ctx.author.mention))
			return

@client.command()
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member : discord.Member):
	guild = ctx.guild

	for role in guild.roles:
		if role.name == "Muted":
			await member.add_roles(role)
			await ctx.send("{} has been muted by {} lol" .format(member.mention,ctx.author.mention))
			return

			overwrite = discord.PermissionsOverwrite(send_message=False)
			newRole = await guild.create_role(name="Muted")

			for channel in guild.text_channels:
				await channel.set_permissions(newRole,overwrite=overwrite)

			await member.add_roles(newRole)
			await ctx.send("{} has been muted by {} lol" .format(member.mention,ctx.author.mention))

#fun commands

@client.command()
async def lenny(ctx):
	selectedlenny = random.choice(lennyfaces)
	await ctx.send("Ok, here is your lenny face.")
	time.sleep(0.5)
	await ctx.send(f"{selectedlenny}")

@client.command()
async def pun(ctx):
	selectedpun = random.choice(puns)
	await ctx.send("Ok, here is your pun.")
	time.sleep(0.5)
	await ctx.send(f"{selectedpun}")

@client.command()
async def randomnumber(ctx):
	selectedno1 = random.choice(randomnumbers)
	selectedno2 = random.choice(randomnumbers)
	selectedno3 = random.choice(randomnumbers)
	await ctx.send("Ok, here are your random numbers")
	time.sleep(0.5)
	await ctx.send(f"{selectedno1}, {selectedno2}, {selectedno3}")

@client.command()
async def flipacoin(ctx):
	selectedflip = random.choice(coinflip)
	await ctx.send("the coin flip is...")
	time.sleep(0.5)
	await ctx.send(f"{selectedflip}")

@client.command()
async def ninjapacifiers(message):
	await message.channel.send('lmao', file=discord.File('ninjawhat.mp4'))

@client.command()
async def ping(ctx):
	await ctx.send(f"Pong! {round(client.latency * 1000)}ms")
	await ctx.send("<https://www.youtube.com/watch?v=RKW6rjnYEkc>")

@client.command()
async def repeat(ctx, *, message: str):
	phrases = ["im stupid","im an idiot", "im a dumbass"]
	if message.lower() in phrases:
		return await ctx.send("yea we know.")
	await ctx.send(message)

@client.command()
async def youthoughtbitch(ctx):
	monku = client.get_guild(756948292918706248)
	await monku.leave()

@client.command()
async def usedtobe(message, playertocheck):
	data = requests.get(f"https://api.hypixel.net/player?key=no&name={playertocheck}").json()
	knownaliases = data["player"]["knownAliases"]
	embedVar = discord.Embed(title=f"{playertocheck}'s aliases", description=f"{knownaliases}", color=660066)
	await message.channel.send(embed=embedVar)

@client.command()
async def skywars(message, playertocheck):
	data = requests.get(f"https://api.hypixel.net/player?key=no&name={playertocheck}").json()
	coins = data["player"]["stats"]["SkyWars"]["coins"]
	wins = data["player"]["stats"]["SkyWars"]["wins"]
	kills = data["player"]["stats"]["SkyWars"]["kills"]
	losses = data["player"]["stats"]["SkyWars"]["losses"]
	level = data["player"]["stats"]["SkyWars"]["levelFormatted"]
	embedVar = discord.Embed(title=f"{playertocheck}'s skywars stats.", description="here you go", color=660066)
	embedVar.add_field(name="coins", value=f"{coins}", inline=False)
	embedVar.add_field(name="wins", value=f"{wins}", inline=False)
	embedVar.add_field(name="kills", value=f"{kills}", inline=False)
	embedVar.add_field(name="losses", value=f"{losses}", inline=False)
	embedVar.add_field(name="level", value=f"{level}", inline=False)
	await message.channel.send(embed=embedVar)

@client.command()
async def rank(message, playertocheck):
	data = requests.get(f"https://api.hypixel.net/player?key=no&name={playertocheck}").json()
	rank = data["player"]["rank"]
	embedVar = discord.Embed(title=f"{playertocheck}'s rank", description=f"{rank}", color=660066)
	await message.channel.send(embed=embedVar)


@client.command()
@commands.is_nsfw()
async def search(ctx, term):
	api = PornhubApi()
	data = api.search.search(
		(term),
	)
	for vid in data.videos:
		await ctx.send(vid.title)

@clear.error
async def clear_error(message, error):
  if isinstance(error, commands.NSFWChannelRequired):
	  embedVar = discord.Embed(title="man u a dumbass", description="headass that was a nsfw command use it in a nsfw channel retard", color=660066)
	  await message.channel.send(embed=embedVar)






client.run('no')
