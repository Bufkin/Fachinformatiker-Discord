# -*- coding: iso-8859-1 -*-
import asyncio
import datetime as datetime
import logging.handlers

import discord
import pytz

intents = discord.Intents.all()
intents.members = True
intents.messages = True
intents.presences = True
client = discord.Client(intents=intents)
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
logging.getLogger('discord.http').setLevel(logging.INFO)

handler = logging.handlers.RotatingFileHandler(
    filename='rollen.log',
    encoding='utf-8',
    maxBytes=32 * 1024 * 1024,  # 32 MiB
    backupCount=5,  # Rotate through 5 files
)
dt_fmt = '%Y-%m-%d %H:%M:%S'
formatter = logging.Formatter(
    '[{asctime}] [{levelname:<8}] {name}: {message}', dt_fmt, style='{')
handler.setFormatter(formatter)
logger.addHandler(handler)


@client.event
async def check_roles():
    for guild in client.guilds:
        for member in guild.members:
            for role in member.roles:
                if role.name == "-undefined-":
                    print(
                        f"USER_ID: {member.id:d} - USER_NAME: {member.name}  - ROLE: {role.name} - Beigetreten {member.joined_at.strftime('%d.%m.%Y')}")
                    created = member.joined_at
                    now = datetime.datetime.today().replace(tzinfo=pytz.UTC)
                    join_und_7_tage = created + datetime.timedelta(days=7)
                    if join_und_7_tage < now:
                        print(f"Benutzer gefunden {member.name:s}")
                        userid = member.id
                        getuser = guild.get_member(userid)
                        channel = client.get_channel(1012434714293968926)
                        await channel.send(f"{member.mention} hat die {role.name} Role seit 7 tagen und wird gekickt")
                        embed = discord.Embed(title="Kick",
                                              description="Du wurdest gekickt weil du keine Rolle in Channel: <#905056217595002891> ausgewählt hast.",
                                              color=0xbd2e2e)
                        embed.set_author(name="Fachinformatiker-Discord")
                        embed.add_field(name="Hinweis",
                                        value="Du kannst wieder joinen, aber wähle eine Rolle innerhalb von 7 Tagen aus. https://discord.gg/DYxRQgwKE4",
                                        inline=False)
                        await getuser.send(embed=embed)
                        await getuser.kick(reason='')
    await asyncio.sleep(60 * 60 * 24)


@client.event
async def update_presence():
    await client.change_presence(activity=discord.Game('https://www.fachinformatiker.de'), status=discord.Status.online)
    await asyncio.sleep(5)
    await client.change_presence(activity=discord.Game('Rollen-Check'), status=discord.Status.online)
    await asyncio.sleep(5)


async def main():
    @client.event
    async def on_ready():
        print("Bot is ready!")
        print("Logged in as: " + client.user.name)
        print("Bot ID: " + str(client.user.id))
        for guild in client.guilds:
            print("Connected to server: {}".format(guild))
        print("------")

        print("Starting up...")
        await client.loop.create_task(update_presence())
        await client.loop.create_task(check_roles())

if __name__ == '__main__':
    asyncio.run(main())
    client.run('')
