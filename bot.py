import discord
import logging
import re
import sched, time
from discord.ext import tasks, commands
import asyncio
import os
import os.path
from os import path
from sys import platform
from datetime import datetime
from sys import platform
import threading
if platform == "linux" or platform == "linux2":
    from gpiozero import CPUTemperature



### IDs
bot_name = "Server Backup by XYI#2691"
bot_id = 675335503012167723
prefix = "."
owner_id = 476348613870616576
mod_id = [566942035182092289]
### VERSIONS
vname = "version:"
mav = 1
miv = 7
pv = 2
vrating = ""
vinfo = " (sorry for the patreon error)"

# varibales to be changed
debug = 0




if debug == 1:
    vinfo = " (DEBUGGING(UNSTABLE))"



class MyClient(discord.Client):


    async def on_ready(self):
        version = str(vname)+" "+str(mav)+"."+str(miv)+"."+str(pv)+str(vrating)+str(vinfo)
        print('Logged on as {0}!'.format(self.user)+" on: "+version)
        await client.change_presence(activity=discord.Game(name=version))
        servers0 = 0
        async for guild in client.fetch_guilds(limit=None):
            servers0 += 1
        while True:
            time.sleep(10)
            server = self.get_guild(675331417932038144)
            channel = self.get_channel(682308104804761782)
            await channel.send("message")


    async def on_message(self, message):



        if message.author.id != (self.user.id):
            print("Message\n")
            with open('community_bot/message.log', 'a') as text3:
                if message.guild is None:
                    form = "direct"+"--"+message.channel.recipient.name+"#"+message.channel.recipient.discriminator+"--"+"\""+message.content.encode('ascii', 'ignore').decode('ascii').replace("\n","--NEWLINE--")+"\""+"\n"
                    ##xy = threading.Thread(target=logging, args=(form,))
                    ##xy.start()
                else:
                    form = "server"+"--"+message.channel.mention+"--"+message.author.name+"#"+message.author.discriminator+"--"+"\""+message.content.encode('ascii', 'ignore').decode('ascii').replace("\n","--NEWLINE--")+"\""+"\n"
                    ##xy = threading.Thread(target=logging, args=(form,))
                    ##xy.start()
        if message.content != "--++--":
            if path.exists("community_bot/ignored/"+str(message.author.id)+".txt") == False:
                if message.author.id != (self.user.id):
                    y = re.findall("dont*|do not*|don't*|don`t*|not*", message.content)
                    with open('community_bot/regex1.txt', 'rt') as text1:
                        textstrip1 = text1.readline().strip()
                        x = re.findall(textstrip1, message.content)
                        if (x):
                            if not y:
                                user = client.get_user(message.author.id)
                                with open('community_bot/reply.txt', 'rt') as text2:
                                    textstrip2 = text2.read().strip()
                                await user.send(textstrip2)





        if message.content == ".status":
            if message.author.id == owner_id or mod_id:
                channel = message.channel
                await channel.send(f'{round(self.latency*1000,2)}ms')

        if message.content == ".stop":
            ignore1 = open("community_bot/ignored/"+str(message.author.id)+".txt", "w+")

        if message.content == ".start":
            os.remove("community_bot/ignored/"+str(message.author.id)+".txt")


        if message.content.startswith(".resources") == True:
                if message.author.id != (self.user.id):
                    if message.mentions != []:
                        print(message.mentions[0].id)
                        user = client.get_user(message.mentions[0].id)
                        with open('community_bot/reply.txt', 'rt') as text2:

                            textstrip2 = text2.read().strip()
                        channel = message.channel
                        await user.send(textstrip2)
                        await channel.send("I sent "+user.name+" resources! Good Luck <3")
                    else:
                        channel = message.channel
                        with open('community_bot/reply.txt', 'rt') as text2:

                            textstrip2 = text2.read().strip()
                        await channel.send(textstrip2)

        if message.content == ".help":
            embed=discord.Embed(title="Help Command", description="SC by XYI", color=0xff0000)
            embed.set_author(name="Help Command")
            embed.add_field(name=".stop", value="stop recieving messages from SC", inline=False)
            embed.add_field(name=".start", value="start recieving messages after using .stop", inline=False)
            embed.add_field(name=".resources", value="get help message in chat                                                  ", inline=True)
            embed.add_field(name=".resources [mention]", value="send help to a user", inline=True)
            embed.add_field(name=".support", value="see ways to contact us", inline=True)
            embed.add_field(name=".breathe", value="breathing gif", inline=True)
            embed.set_footer(text="© 2019-2020 XYI Development Team")
            channel = message.channel
            await channel.send(embed=embed)
            
        if message.content == ".support":
            embed=discord.Embed(title="support server", url="https://discord.gg/kabDPUg", description="SC by XYI", color=0xff0000)
            embed.set_author(name="Support Command", url="https://discord.gg/kabDPUg")
            embed.add_field(name="Discord", value="Contact us using Discord | discord.gg/kabDPUg", inline=True)
            embed.add_field(name="Message Developer", value="!mirandaniel#3515 | $snoewy#8119", inline=True)
            embed.set_footer(text="© 2019-2020 XYI Development Team")
            channel = message.channel
            await channel.send(embed=embed)

        if message.content == ".breathe":
            embed=discord.Embed(title="Breathe GIF", url="https://i.giphy.com/media/krP2NRkLqnKEg/giphy.webp", description="SC by XYI", color=0xff0000)
            embed.set_author(name="Breathe GIF", url="https://i.giphy.com/media/krP2NRkLqnKEg/giphy.webp")
            embed.set_footer(text="© 2019-2020 XYI Development Team")
            channel = message.channel
            await channel.send(embed=embed)

        if message.content.startswith(".emergency"):
            if message.author.id != (self.user.id):
                    if message.mentions != []:
                        print(message.mentions[0].id)
                        user = client.get_user(message.mentions[0].id)
                        with open('community_bot/replyem.txt', 'rt') as text3:

                            textstrip3 = text3.read().strip()
                        channel = message.channel
                        await user.send(textstrip3)
                        await channel.send("I sent "+user.name+" emergency resources! Good Luck <3")
                    else:
                        channel = message.channel
                        with open('community_bot/replyem.txt', 'rt') as text3:

                            textstrip3 = text3.read().strip()
                        await channel.send(textstrip3)

        if message.content == ".admin":
            if message.author.id == owner_id:
                time = str(datetime.now().strftime("%Y-%m-%d"))
                
                statinfo = os.stat("community_bot/logging/message/"+time+"mdata.log")

                if platform == "linux" or platform == "linux2":
                    cpu = CPUTemperature()
                    await message.channel.send(
                    "Log size = "+str(statinfo.st_size/1000/1000)+"MB"+" ("+str(statinfo.st_size/1000)+"kb"+")"+"\n"
                    "Platform = "+str(platform)+"\n"
                    "Ping = "+str(f'{round(self.latency*1000,2)}ms')+"\n"
                    "Temp = "+str(cpu.temperature)
                    )
                else:
                    await message.channel.send(
                    "Log size = "+str(statinfo.st_size/1000/1000)+"MB"+" ("+str(statinfo.st_size/1000)+"kb"+")"+"\n"
                    "Platform = "+str(platform)+"\n"
                    "Ping = "+str(f'{round(self.latency*1000,2)}ms')+"\n"
                    )
            
        if message.content == ".donator":
            server = self.get_guild(677877171032686593)
            author = server.get_member(message.author.id)
            donator = author.roles[1]
            level = author.roles[2]
            ranks = ["plus","premium","extra","beta access"]
            if str(level) in str(ranks):
                channel = message.channel
                await channel.send("You are a "+str(level)+" donator.")
            else:
                if str(donator) == "donator" or "XYI premium membership":
                    channel = message.channel
                    await channel.send("You are a donator.")
                else:
                    channel = message.channel
                    await channel.send("You are not a donator. You can donate using \donate or \patreon")

def logging(data):
    time = str(datetime.now().strftime("%Y-%m-%d"))
    prextime = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    with open("community_bot/logging/message/"+time+"mdata.log", "a") as msglog:
        msglog.write(prextime+" "+data)




client = MyClient()
with open('community_bot/data/token.token') as token:
    token_ready = token.read().strip()
client.run(token_ready)
