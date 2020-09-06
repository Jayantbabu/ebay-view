import discord
import random
from discord.ext import commands
import datetime

client = commands.Bot(command_prefix = '>', description="Ebay View Bot", case_insensitive=True)

log_channel_id = 727218642575556708

client.embed_color = discord.Color.from_rgb(231, 231, 192)
client.footer = "Your mom."
client.footer_image = "https://pbs.twimg.com/media/EVmo6vpWsAQxl3j.jpg"

@client.command(aliases=['8ball'], help = "Gives a reading on your future!")
async def _8ball(ctx, *, question):
    responses = ['no',
                 'yes']
    embed = discord.Embed(
        title = f"Question: {question}\nAnswer: {random.choice(responses)}",
        color = client.embed_color,
        timestamp = datetime.datetime.now(datetime.timezone.utc)
    )
    embed.set_footer(
        text = client.footer,
        icon_url = client.footer_image,
    )
    client.log_channel = client.get_channel(log_channel_id)
    await client.log_channel.send(embed = embed)

@client.event
async def on_ready():
    print(f"Logged in as {client.user} and connected to Discord (ID: {client.user.id})")

    game = discord.Game(name = ">help")
    await client.change_presence(activity = game)

    embed = discord.Embed(
        title = f"{client.user.name} ONLINE!",
        color = discord.Color.from_rgb(231, 231, 192),
        timestamp = datetime.datetime.now(datetime.timezone.utc)
    )
    embed.set_footer(
        text = client.footer,
        icon_url = client.footer_image
    )
    client.log_channel = client.get_channel(log_channel_id)
    await client.log_channel.send(embed = embed)

@client.command(name = "restart", aliases=['r'], help = "Restarts the bot")
async def restart(ctx):
    embed = discord.Embed(
        title = f"{client.user.name} Restarting",
        color = client.embed_color,
        timestamp = datetime.datetime.now(datetime.timezone.utc)
    )
    embed.set_author(
        name = ctx.author.name,
        icon_url = ctx.author.avatar_url
    )
    embed.set_footer (
        text = client.footer,
        icon_url = client.footer_image,
    )
    client.log_channel = client.get_channel(log_channel_id)
    await client.log_channel.send(embed = embed)

    await ctx.message.add_reaction('✅')
    await client.close()


client.run('NzI3MjE4MzMxNjM1MTU0OTk1.Xvoo2Q.jRYOUqQ2ifGWnQIIGGMkBudbIvo', bot=True)
