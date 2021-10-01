import discord
import setting
import requests

BOT_TOKEN = setting.BOT_TOKEN
BITLY_TOKEN = setting.BITLY_TOKEN

client = discord.Client()

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


def shortenURL(longUrl):
    url = "https://api-ssl.bitly.com/v3/shorten"
    access_token = BITLY_TOKEN
    query = {
        'access_token' : access_token,
        'longUrl': longUrl
    }

    request = requests.get(url, params=query).json()['data']['url']
    return request

client.run(BOT_TOKEN)
