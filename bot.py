from pyrogram import Client
import os

BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
API_ID = int(os.environ.get("API_ID", "7984040"))
API_HASH = os.environ.get("API_HASH", "153fb8518916a808ce50ec01fd2b35b3")

if __name__ == "__main__" :
    plugins = dict(
        root="plugins"
    )
    bot = Client(
        "Lilly-muzic",
        bot_token=BOT_TOKEN,
        api_hash=API_HASH,
        api_id=API_ID,
        plugins=plugins
    )
    bot.run()
