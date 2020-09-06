import discord
import requests
import time, datetime
import os, sys, logging
from discord.ext import commands
from linkpreview import link_preview

bot = commands.Bot(command_prefix="-", description="ebay-view-bot", case_insensitive=True)

log_channel_id = 751991759025864794
bot.footer_image = "https://1000logos.net/wp-content/uploads/2018/08/eBay-Logo.png"
bot.footer = "ebay-view-bot"

@bot.command(aliases=['ebay'], help = "Give the link and number of views")
async def view(ctx, link, number):
	embed = discord.Embed(
				title = f'Gave {number} views to the {link}',
				color = discord.Color.from_rgb(68, 128, 123),
				timestamp = datetime.datetime.now(datetime.timezone.utc)
				 )
	bot.foot = link_preview(link, requests.get(link).content.decode("utf-8")).image
	embed.set_image(url=bot.foot)
	bot.log_channel = bot.get_channel(log_channel_id)
	for num in range(int(number)):
		requests.get(link)
		print(num)
	await bot.log_channel.send(embed = embed)


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
	embed.set_image(url=bot.footer_image)
	bot.log_channel = bot.get_channel(log_channel_id)
	await bot.log_channel.send(embed = embed)

if __name__ == "__main__":
		bot.run('NzUxOTY3Nzk0MjkxMDE1Nzcy.X1QylQ.12uwrSqef_Vllv5ZGHZ39Tc-p-M', bot=True, reconnect=True)
