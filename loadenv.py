import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(verbose=True, dotenv_path=dotenv_path)

TOKEN = os.getenv('DISCORD_TOKEN')
