from pyrogram import Client
import os

BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")

if __name__ == "__main__" :
    plugins = dict(
        root="plugins"
    )
    bot = Client(
        "YT-Muzic",
        bot_token=BOT_TOKEN,
        api_hash=API_HASH,
        api_id=API_ID,
        plugins=plugins
    )
    bot.run()
