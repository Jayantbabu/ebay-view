import discord
import requests
import time, datetime
import os, sys, logging
from discord.ext import commands
from linkpreview import link_preview

bot = commands.Bot(command_prefix="-", description="ebay-view-bot", case_insensitive=True)

log_channel_id = 751991759025864794

bot.footer = "ebay-view-bot"

@bot.command(aliases=['ebay'], help = "Give the link and number of views")
async def ebay_view(ctx, link, number):
	embed = discord.Embed(
				title = f'Giving {number} views to the {link}',
				color = discord.Color.from_rgb(68, 128, 123),
				timestamp = datetime.datetime.now(datetime.timezone.utc)
				 )

	embed.set_footer(icon_url = link_preview(link, requests.get(link).content.decode("utf-8")).image)
	bot.log_channel = bot.get_channel(log_channel_id)
	for num in range(number):
		await requests.get(link)


@bot.event
async def on_ready():
	print(f"Logged in as {bot.user} and connected to Discord (ID: {bot.user.id})")
	game = discord.Game(name = ">help")
	await bot.change_presence(activity = game)

	embed = discord.Embed(
			title = f"{bot.user.name} ONLINE!",
			color = discord.Color.from_rgb(68, 128, 123),
			timestamp = datetime.datetime.now(datetime.timezone.utc)
			)
	embed.set_footer(
			icon_url = "https://pbs.twimg.com/media/EVmo6vpWsAQxl3j.jpg"
			)
	bot.log_channel = bot.get_channel(log_channel_id)
	await bot.log_channel.send(embed = embed)

if __name__ == "__main__":
		bot.run('NzUxOTY3Nzk0MjkxMDE1Nzcy.X1QylQ.12uwrSqef_Vllv5ZGHZ39Tc-p-M',  reconnect=True)
