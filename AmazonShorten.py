import discord
import setting

API_TOKEN = setting.API_TOKEN

client = discord.Client()

@client.event
async def on_ready():
    print('ログインしました')


client.run(API_TOKEN)

