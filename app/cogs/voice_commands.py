import asyncio
import discord
from pytube import Search
from pytube import YouTube
from discord import app_commands
from discord.ext import commands
import yt_dlp
import requests
from app.classes.youtube_class import (
    vid_link,
    download_vid,
    delete_audio,
    find_music_name,
    remove_all_files,
)


GUILD_ID = discord.Object(id=458722730641063936)


class Voice_Commands(commands.Cog):
    """Cog for voice commands"""

    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="join_voice")
    async def join_voice(self, interaction: discord.Interaction):
        if interaction.user.voice:
            print(interaction.user.display_name)
            channel = interaction.user.voice.channel  # getting voice channel name
            await channel.connect()
            await interaction.response.send_message(
                f"Joined {channel.name}", ephemeral=True
            )
        else:
            await interaction.response.send_message(
                "You need to join a voice channel first", ephemeral=True
            )

    @app_commands.command(name="leave_voice")
    async def leave_voice(self, interaction: discord.Interaction):
        if interaction.guild.voice_client:
            await interaction.guild.voice_client.disconnect()
            await interaction.response.send_message(
                "Left voice channel", ephemeral=True
            )
            # remove_all_files(dir="app/music")
        else:
            await interaction.response.send_message(
                "I am not in a voice channel", ephemeral=True
            )

    @app_commands.command(name="pause")
    async def pause_music(self, interaction: discord.Interaction):
        if (
            interaction.guild.voice_client
            and interaction.guild.voice_client.is_playing()
        ):
            interaction.guild.voice_client.pause()
            await interaction.response.send_message("Music Paused", ephemeral=True)
        else:
            await interaction.response.send_message(
                "I am not playing anything", ephemeral=True
            )

    @app_commands.command(name="resume")
    async def resume_music(self, interaction: discord.Interaction):
        if (
            interaction.guild.voice_client
            and interaction.guild.voice_client.is_paused()
        ):

            interaction.guild.voice_client.resume()
            await interaction.response.send_message("Music resumed", ephemeral=True)
        else:
            await interaction.response.send_message(
                "I am not playing anything", ephemeral=True
            )

    @app_commands.command(name="play")
    async def play_music(self, interaction: discord.Interaction, *, title: str):
        try:
            if not interaction.guild.voice_client:
                channel = interaction.user.voice.channel
                vc = await channel.connect()
                await interaction.response.send_message(f"Joined {vc.channel.name} , Playing {title} ...")
                download_vid(title)
                # await interaction.response.send_message(f'Preparing to Play : {find_music_name()}') #sending confirmation
                # async with vc.channel.typing():
                vc.play(
                    discord.FFmpegPCMAudio(
                        executable="/usr/bin/ffmpeg",
                        source=f"app/music/{find_music_name()}",  # The audio file path
                        options="-vn -filter:a equalizer=f=1000:t=q:w=1:g=0.5",  # Apply equalizer with reduced gain
                        before_options="-re"  # This tells FFmpeg to read at the real-time rate (to reduce latency)
                    ),
                    after=lambda e: print(f"Playback ended with error: {e}") or asyncio.run_coroutine_threadsafe(vc.disconnect(), self.bot.loop)
                )
                while vc.is_playing() or vc.is_paused():
                    await asyncio.sleep(1)

                remove_all_files(dir="app/music")
        except Exception as e:
            print(e)
            await interaction.response.send_message(
                "Error playing music", ephemeral=True
            )

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"voice commands setup up after {self.bot.user.name} the server")


async def setup(bot):
    await bot.add_cog(Voice_Commands(bot))


if __name__ == "__main__":
    pass

# # await interaction.response.send_message(download_vid(title))
        # # channel = interaction.user.voice.channel
        # # if not interaction.guild.voice_client:
        # #     vc = await channel.connect()
#     async with vc.typing():
        #      vc.play(
        #         discord.FFmpegPCMAudio(
        #             executable="/usr/bin/ffmpeg",
        #             source=f"app/music/{find_music_name()}",  # The audio file path
        #              options="-vn -filter:a equalizer=f=1000:t=q:w=1:g=0.5",  # Apply equalizer with reduced gain
        #              before_options="-re"  # This tells FFmpeg to read at the real-time rate (to reduce latency)
        #         )
        #     )
        #     # interaction.guild.voice_client.play(player, after=lambda e: print('Player error: %s' % e) if e else None)
        #     await interaction.response.send_message(f'Preparing to Play : {find_music_name()}') #sending confirmmation