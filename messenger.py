import os
import discord
from discord.ext import commands

key = os.environ['TOKEN']

OWN_ID = os.environ['ID']

def_msg = open("message.txt","r").read()

bot = commands.Bot(command_prefix='!')

@bot.command()
async def dm(ctx, user: discord.User, *,message):
    if message == "1":
        await user.send(def_msg)
    else:
        await user.send(message)

@bot.event
async def on_message(message):
    await bot.process_commands(message)
    if message.author.bot:
        return
    if isinstance(message.channel, discord.DMChannel):    #CHECKS IF MESSAGE IS IN DM
        owner = bot.get_user(OWN_ID)
        print(
            f"{message.author.name}#{message.author.discriminator} <{message.author.id}>: {message.content}"
        )
        await owner.send(
            f"{message.author.name}#{message.author.discriminator} <{message.author.id}>: {message.content}"
        )   #SENDS THE MESSAGE SENT TO THE BOT, TO THE OWNER
	
bot.run(key)