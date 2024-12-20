import discord
from pytube import Search
from pytube import YouTube
from discord import app_commands
from discord.ext import commands
import yt_dlp
import requests
import shutil
import os


def vid_link(title):  # function needs optimization **
        search_url = Search(f"{title}")
        youTube_ids = search_url.results
        video_ids = [vid_id for vid_id in youTube_ids]

        vidd_id = video_ids[0]
        base_url = f"https://www.youtube.com/watch?v={vidd_id}"
        return base_url


def download_vid(title, save_folder='app/music'):
    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': f'{save_folder}/%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',  # Use FLAC for better quality
                'nopostoverwrites': False,
            }],
            'ffmpeg_location': '/usr/bin/ffmpeg',
            'quiet': False,
            'extractaudio': True,
            'noplaylist': True,
        }

        # Use yt-dlp to search for the video based on the title
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            result = ydl.extract_info(f"ytsearch:{title}", download=True)  # The search term is 'ytsearch:'
            
            # Check if there are search results and download the first one
            if 'entries' in result:
                video = result['entries'][0]  # Get the first video
                return print(f"Downloading: {video['title']}")

            else:
                print("No results found for the search term.")
                
    except Exception as e:
        print(f"Error: {e}")


def delete_audio():
        shutil.rmtree("music")

def find_music_name():
        return os.listdir("app/music")[0]

def remove_all_files(*,dir):
        for f in os.listdir(dir):
            os.remove(os.path.join(dir, f))


if __name__ == "__main__":
    pass
