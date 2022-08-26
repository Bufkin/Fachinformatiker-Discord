# -*- coding: iso-8859-1 -*-
import asyncio
import discord
import datetime
import logging
import discord_emoji
from discord import Member, channel, message
from discord.ext.commands import MissingPermissions, bot, has_permissions

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
        await channel.send(f'**Hey! {member.name}**\n Willkommen auf dem Discord Server von Fachinformatiker! \n Viel SpaÃƒÅ¸!')


@client.event
async def on_message(message):
    global g

    if message.author.bot:
        return
    if message.content.lower() == "!help":
        await message.channel.send('**Hilfe zum Fachinformatiker-Bot**\n\n'
                                   '$help zeigt diese Hilfe an.')

@client.event
async def on_reaction_add(reaction, member):
    Channel = client.get_channel(905056217595002891)
    if reaction.message.channel.id != Channel.id:
        return
    if reaction.emoji == '\N{keyboard}':
        role = discord.utils.get(member.guild.roles, name="FIDV")
        await member.add_roles(role)
    if reaction.emoji == '\N{telescope}':
        role = discord.utils.get(member.guild.roles, name="FIDV-Azubi")
        await member.add_roles(role)
    if reaction.emoji == '\N{wrench}':
        role = discord.utils.get(member.guild.roles, name="FIDP-Azubi")
        await member.add_roles(role)
    if reaction.emoji == '\N{screwdriver}':
        role = discord.utils.get(member.guild.roles, name="FIDP")
        await member.add_roles(role)
    if reaction.emoji == '\N{ticket}':
        role = discord.utils.get(member.guild.roles, name="FIAE-Azubi")
        await member.add_roles(role)
    if reaction.emoji == '\N{Notebook}':
        role = discord.utils.get(member.guild.roles, name="FIAE")
        await member.add_roles(role)
    if reaction.emoji == '\N{Personal Computer}':
        role = discord.utils.get(member.guild.roles, name="FISI-Azubi")
        await member.add_roles(role)
    if reaction.emoji == '\N{Desktop Computer}':
        role = discord.utils.get(member.guild.roles, name="FISI")
        await member.add_roles(role)

@client.event
async def on_reaction_remove(reaction, user):
    Channel = client.get_channel(905056217595002891)
    if reaction.message.channel.id != Channel.id:
        return
    if reaction.emoji == '\N{keyboard}':
        role = discord.utils.get(member.guild.roles, name="FIDV")
        await member.remove_roles(role)
    if reaction.emoji == '\N{telescope}':
        role = discord.utils.get(member.guild.roles, name="FIDV-Azubi")
        await member.remove_roles(role)
    if reaction.emoji == '\N{wrench}':
        role = discord.utils.get(member.guild.roles, name="FIDP-Azubi")
        await member.remove_roles(role)
    if reaction.emoji == '\N{screwdriver}':
        role = discord.utils.get(member.guild.roles, name="FIDP")
        await member.remove_roles(role)
    if reaction.emoji == '\N{ticket}':
        role = discord.utils.get(member.guild.roles, name="FIAE-Azubi")
        await member.remove_roles(role)
    if reaction.emoji == '\N{Notebook}':
        role = discord.utils.get(member.guild.roles, name="FIAE")
        await member.remove_roles(role)
    if reaction.emoji == '\N{Personal Computer}':
        role = discord.utils.get(member.guild.roles, name="FISI-Azubi")
        await member.remove_roles(role)
    if reaction.emoji == '\N{Desktop Computer}':
        role = discord.utils.get(member.guild.roles, name="FISI")
        await member.remove_roles(role)

def main():
    @client.event
    async def on_ready():
        global g
        print("Bot is ready!")
        print("Logged in as: " + client.user.name)
        print("Bot ID: " + str(client.user.id))
        for guild in client.guilds:
            print("Connected to server: {}".format(guild))
        print("------")
        client.loop.create_task(status_task())
        channels = client.get_channel(905056217595002891)
        print('Clearing messages...')
        await channels.purge(limit=1000)
        embed = discord.Embed(title='Wähle die Fachrichtung deines Fachinformatikers!',
                                          description='Auswahl des Fachbereiches')
        embed.add_field(name='Systemintegeration', value='\N{Desktop Computer}', inline=True)
        embed.add_field(name='Systemintegeration-Azubi', value='\N{Personal Computer}', inline=True)
        embed.add_field(name='Anwendungsentwicklung', value='\N{Notebook}', inline=True)
        embed.add_field(name='Anwendungsentwicklung-Azubi', value='\N{ticket}', inline=True)
        embed.add_field(name='Digitale Vernetzung', value='\N{screwdriver}', inline=True)
        embed.add_field(name='Digitale Vernetzung-Azubi', value='\N{wrench}', inline=True)
        embed.add_field(name='Daten- und Prozessanalyse', value='\N{keyboard}', inline=True)
        embed.add_field(name='Daten- und Prozessanalyse-Azubi', value='\N{telescope}', inline=True)
        embed.set_footer(text='Auswahl ist erforderlich')
        mess = await channels.send(embed=embed)
        await mess.add_reaction('\N{Desktop Computer}')
        await mess.add_reaction('\N{Personal Computer}')
        await mess.add_reaction('\N{Notebook}')
        await mess.add_reaction('\N{ticket}')
        await mess.add_reaction('\N{screwdriver}')
        await mess.add_reaction('\N{wrench}')
        await mess.add_reaction('\N{keyboard}')
        await mess.add_reaction('\N{telescope}')


        



if __name__ == '__main__':
    main()

client.run('')
