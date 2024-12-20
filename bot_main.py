import asyncio
import random
from typing import Annotated
import discord
from app.config.config import TOKEN
from discord.ext import commands
from discord import app_commands
import logging

handler = logging.FileHandler(filename="./logs/Discord.log", encoding="utf-8", mode="a")

GUILD_IDS = [discord.Object(id=458722730641063936),discord.Object(id=1289677784775528531)]

class MyBot(commands.Bot):
    def __init__(self, command_prefix, intents):
        super().__init__(command_prefix=command_prefix,intents=intents)

    async def setup_hook(self):
        """This method is called before the bot connects to Discord."""
        try:
            # Load the main_commands cog
            await self.load_extension('app.cogs.main_commands')
            await self.load_extension('app.cogs.voice_commands')
            print("Cogs loaded successfully.")

            # Make commands specefic for guild with guild id
            for guild in GUILD_IDS:
                self.tree.copy_global_to(guild=guild)
                await self.tree.sync(guild=guild)
            # self.tree.copy_global_to(guild=GUILD_ID)
            # Sync/register commands for the specified guild
            # await self.tree.sync(guild=GUILD_ID)
            # await self.tree.sync() # Syncing commands in all servers (may take some time)
            print("Commands synced successfully.")
        except Exception as e:
            print(f"Failed to load cog: {e}")

intents = discord.Intents.default()
intents.message_content = True

bot = MyBot(command_prefix='!',intents=intents)


bot.run(TOKEN,log_handler=handler,log_level=logging.DEBUG)


















# counter = 0
# # 458722730641063936


# @bot.tree.command(
#     name="hello", description="AtlasBot says hello to you", guild=GUILD_ID
# )
# async def hellocommand(interaction: discord.Interaction):
#     await interaction.response.send_message("Hello to you")


# # @bot.tree.command(
# #     name="rolldice", description="Roll a number from the Dice", guild=GUILD_ID
# # )
# # @app_commands.describe(number="The number to roll")
# # async def roll_dice(interaction: discord.Interaction, number: int):
# #     await interaction.response.send_message(f"Dice rolled is {number}")


# # @bot.tree.command(name="about", description="About Me", guild=GUILD_ID)
# # async def aboutcommand(interaction: discord.Interaction):
# #     await interaction.response.send_message(
# #         f"im atlasbot and im in work progress to something amazing"
# #     )


# # @bot.tree.command(name="referal", description="refering", guild=GUILD_ID)
# # async def referalcommand(interaction: discord.Interaction):
# #     await interaction.response.send_message(f"referiiiiiiiiiiiing!!!!")


# @bot.tree.command(name="sync", description="Dev purposes Dont use", guild=GUILD_ID)
# async def synccommand(interaction: discord.Interaction):
#     try:
#         member = interaction.guild.get_member(interaction.user.id)
#         if member:
#             roles = member.roles
#             if any(role.name == "Dev-bot" for role in roles):
#                 guild = discord.Object(id=458722730641063936)
#                 synced = await bot.tree.sync(guild=guild)
#                 cm_list = bot.tree.get_commands()
#                 commands = [command.name for command in cm_list]
#                 await interaction.response.send_message(
#                             f"{commands} Synced {len(synced)} commands for {guild.id} , Commands synced successfully!"
#                         )
#             else:
#                 await interaction.response.send_message(
#                             f"you are not allowed to use this command"
#                         )
#     except discord.HTTPException as e:
#         if e.code == 50035:  # Rate limit error code
#             await interaction.response.send_message(
#                 f"Rate limit exceeded. Please try again later."
#             )
#         else:
#             await interaction.response.send_message(f"Failed to sync commands: {e}")


# @bot.tree.command(name="test", description="Printing Test!", guild=GUILD_ID)
# async def testcommand(interaction: discord.Interaction):
#     await interaction.response.send_message("TEEEEST!!!!")


# @bot.event
# async def on_ready():
#         # try:
#         #     guild = discord.Object(id=458722730641063936)
#         #     sync = await bot.tree.sync(guild=guild)
#         #     print(f"synced {len(sync)} for guild {guild.id}")
#         # except Exception as e:
#         #     print(f"something went wrong {e}")
#     print(f"{bot.user.name} Connected to the server")