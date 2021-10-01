import discord
import settings
import shorten
BOT_TOKEN = settings.BOT_TOKEN

client = discord.Client()
shortenURL = shorten.shortenURL
@client.event
async def on_ready():
    print('ログインしました')

@client.event
async def on_message(message):
    if message.author.bot:
        return

    if 'https://www.amazon' in message.content:
        url = shortenURL(message.content)
        await message.channel.send(url)

client.run(BOT_TOKEN)
