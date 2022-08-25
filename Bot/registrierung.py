import asyncio
import logging

import discord

intents = discord.Intents.all()
intents.members = True
intents.messages = True
intents.presences = True
client = discord.Client(intents=discord.Intents.all())
g = client.get_guild(904846660256022579)
logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


@client.event
async def status_task():
    while True:
        await client.change_presence(activity=discord.Game('https://www.fachinformatiker.de'), status=discord.Status.online)
        await asyncio.sleep(10)
        await client.change_presence(activity=discord.Game('User-Bot'), status=discord.Status.online)
        await asyncio.sleep(5)


@client.event
async def on_member_join(member: discord.Member):
    role = discord.utils.get(member.guild.roles, name="-undefined-")
    channel = client.get_channel(905056217595002891)
    if member.guild.id == 904846660256022579:
        await member.add_roles(role)
        await channel.send(f'**Hey! {member.name}**\n Willkommen auf dem Discord Server von Fachinformatiker! \n Viel SpaÃŸ!')


@client.event
async def on_message(message):
    global g




    if message.author.bot:
        return
    if message.content.lower() == "!help":
        await message.channel.send('**Hilfe zum Fachinformatiker-Bot**\n\n'
                                   '$help zeigt diese Hilfe an.')


client.run('MTAxMjQzMDI5MDA4MzQwMTczOA.Gt3S7m.R3NA31EEJqQeJ2jolBuw8k-bpoOopaREU1A0ko')
