import discord
import setting

API_TOKEN = setting.API_TOKEN

client = discord.Client()

@client.event
async def on_ready():
    print('ログインしました')

@client.event
async def on_message(message):
    if message.author.bot:
        return

    if 'https://www.amazon' in message.content:
        await message.channel.send(" Detected Amazon's Link ")
client.run(API_TOKEN)
