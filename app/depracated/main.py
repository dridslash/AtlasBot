import random
from typing import Annotated
import discord
from config import Server_name, TOKEN
from discord.ext import commands
from discord import app_commands


intents = discord.Intents.all()


client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix="!", intents=intents,
                   case_insensitive=False,)


@client.event
async def on_ready():
    print(f"{client.user.name}  connected to the server!")


# @bot.tree.command(name="helloworld", description="Says hello!")
# async def hello_command(interaction: discord.Interaction):
#     await interaction.response.send_message(f"Hello, {interaction.user.mention}!")


# @bot.tree.command(name="whoarewe", description="Gives info about the Mission of our Team")
# async def Whoweare(interaction: discord.Interaction, user: discord.Member):
#     await interaction.response.send_message(
#         f"Hello {user.mention} we are {interaction.guild.name} we make mvps Hopefully and we help people to come up with solutions"
#     )

# @bot.command(name="sync")
# async def sync_command(ctx):
#     await bot.tree.sync()
#     await ctx.send('Command tree synced.')


# @bot.command(name="creat-channel")
# @commands.has_role(".")
# async def create_channel(context, channel_name=Annotated(str, "default-dumb")):
#     guild = context.guild
#     existing_channel = discord.utils.get(guild.channels, name=channel_name)
#     if not existing_channel:
#         print(f"created a channel with name {channel_name} in {guild.name}")
#         await guild.create_text_channel(channel_name)


# @client.event
# async def on_ready():
#     # for guild in client.guilds:
#         # if(guild.name == Server_name):print(guild)
#     # guild = discord.utils.find(lambda gl : gl.name == Server_name,client.guilds)
#     # guild = discord.utils.get(client.guilds,name=Server_name)
#     # members = '\n ->'.join([mems.display_name for mems in guild.members])
#     # print(members)
#     print(f'{client.user.name} has connected to Discord!')

# @client.event
# async def on_message(message):
#     if (message.author == client.user):
#         return
#     info = f"Hello {message.author.display_name} we are AtlasDeploy we work on mvps and we creat solutions that help people"
#     if message.content and message.content.lower() == 'whoweare':
#         response = info
#         await message.channel.send(response)
# @client.event
# async def on_member_join(member):
#     await member.create_dm()
#     await member.dm_channel.send(
#         f'Hi and Welcome to the Discord Server'
#     )

client.run(TOKEN)
