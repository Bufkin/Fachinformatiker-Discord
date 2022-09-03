# -*- coding: iso-8859-1 -*-
import asyncio
import datetime as datetime

import discord
import pytz

intents = discord.Intents.all()
intents.members = True
intents.messages = True
intents.presences = True
client = discord.Client(intents=discord.Intents.all())

@client.event
async def status_task():
    while True:
        await client.change_presence(activity=discord.Game('https://www.fachinformatiker.de'), status=discord.Status.online)
        await asyncio.sleep(5)
        await client.change_presence(activity=discord.Game('Rollen-Check'), status=discord.Status.online)
        await asyncio.sleep(5)
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
                            await channel.send(f"{member.name} hat die {role.name} Role seit 7 tagen und wird gekickt")
                            embed = discord.Embed(title="Kick",
                                                  description="Du wurdest gekickt weil du keine Rolle in Channel: <#905056217595002891> ausgew�hlt hast.",
                                                  color=0xbd2e2e)
                            embed.set_author(name="Fachinformatiker-Discord")
                            embed.add_field(name="Hinwei�",
                                            value="Du kannst wieder joinen, aber w�hle eine Rolle innerhalb von 7 Tagen aus. https://discord.gg/DYxRQgwKE4",
                                            inline=False)
                            await getuser.send(embed=embed)
                            await getuser.kick(reason='')
def main():
    @client.event
    async def on_ready():
        client.loop.create_task(status_task())

if __name__ == '__main__':
    main()


client.run('MTAxNTI5NTczMjE0MTUzNTIzMg.GJp8BV.Ecal6riAb-3RFwuuekUlBiB2WlFlX8a5lfVmEw')