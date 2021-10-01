<<<<<<< HEAD:settings.py
import os
from os.path import join, dirname

from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

BOT_TOKEN= os.environ.get("BOT_TOKEN")
=======
import os
from os.path import join, dirname

from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

BOT_TOKEN= os.environ.get("BOT_TOKEN")
>>>>>>> 1f6b51395f3b0d533a00266e8b6df6fe1a72a1b3:setting.py
BITLY_TOKEN = os.environ.get("BITLY_TOKEN")