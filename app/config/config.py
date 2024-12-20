import os
from dotenv import load_dotenv

load_dotenv(override=True)
TOKEN = os.getenv('DISCORD_TOKEN')
Server_name = os.getenv('GUILD')

if __name__ == '__main__':
    pass