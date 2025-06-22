#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "25342719"))
API_HASH = environ.get("API_HASH", "f4d7a4a9265404c5b94c1793b8144088")
BOT_TOKEN = environ.get("BOT_TOKEN", "8021704971:AAFgtCsQN9N2gq-6iv9p085xJ0d13u5SVNk")
OWNER = int(environ.get("OWNER", "1184337448"))
CREDIT = "𝙎𝘼𝙄𝙉𝙄 𝘽𝙊𝙏𝙎"
AUTH_USER = os.environ.get('AUTH_USERS', '1184337448').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
