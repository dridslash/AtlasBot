import discord
from discord import app_commands
from discord.ext import commands
import requests


GUILD_ID = discord.Object(id=458722730641063936)


class MainCommands(commands.Cog):
    """Class Cog for implementing Cog module"""

    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="hello", description="AtlasBot says hello to you")
    async def hellocommand(self, interaction: discord.Interaction):
        await interaction.response.send_message("Hello to you")

    @app_commands.command(name="rolldice", description="Roll a number from the Dice")
    @app_commands.describe(number="The number to roll")
    async def roll_dice(self, interaction: discord.Interaction, number: int):
        await interaction.response.send_message(f"Dice rolled is {number}")
    @app_commands.command(name="getcurrencyrate",description="Get the currency rate of the given currency")
    @app_commands.describe(currency="The currency to get the rate" , conversion_currency="The currency you want to convert to")
    async def get_currencycommand(self, interaction: discord.Interaction, currency:str , conversion_currency:str):
        try:
            response = requests.get(f"https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/{currency.lower()}.json")
            response.raise_for_status()
            curr = response.json()
            data = {
            "date": curr["date"],
            "currency": currency,
            "rate": curr[currency.lower()][conversion_currency.lower()],
            }
            await interaction.response.send_message(f"your currency rate of {currency} to {conversion_currency} is {data['rate']}💹")
        except Exception as e:
            await interaction.response.send_message(f"Error: {e}")

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.bot.user.name} Connected to the server")

    """Depracated Command"""
    """
    @app_commands.command(name="sync", description="Dev purposes Dont use")
    async def synccommand(self,interaction: discord.Interaction):
        try:
            member = interaction.guild.get_member(interaction.user.id)
            if member:
                roles = member.roles
                if any(role.name == "Dev-bot" for role in roles):
                    guild = discord.Object(id=458722730641063936)
                    synced = await self.bot.tree.sync(guild=guild)
                    cm_list = self.bot.tree.get_commands()
                    commands = [command.name for command in cm_list]
                    await interaction.response.send_message(
                                f"{commands} Synced {len(synced)} commands for {guild.id} , Commands synced successfully!"
                            )
                else:
                    await interaction.response.send_message(
                                f"you are not allowed to use this command"
                            )
        except discord.HTTPException as e:
            if e.code == 50035:  # Rate limit error code
                await interaction.response.send_message(
                    f"Rate limit exceeded. Please try again later."
                )
            else:
                await interaction.response.send_message(f"Failed to sync commands: {e}")
    """


"""Set up bot with Cog (gets called in load_extension())"""


async def setup(bot):
    await bot.add_cog(MainCommands(bot))

if __name__ == '__main__':
    pass