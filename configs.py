import os

class Config(object):
	API_ID = int(os.environ.get("API_ID", "14553761"))
	API_HASH = os.environ.get("API_HASH", "a1cab49dcdfd2eb3bea5e5a552c5d479")
	BOT_TOKEN = os.environ.get("BOT_TOKEN", "Bot Token")
	BOT_USERNAME = os.environ.get("BOT_USERNAME", "Bot Name")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "DB Channel ID"))
	BOT_OWNER = int(os.environ.get("BOT_OWNER", "604152966"))
	DATABASE_URL = os.environ.get("DATABASE_URL", "Mongo DB URL")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "")
	LOG_CHANNEL = os.environ.get("LOG_CHANNEL", "Log Channel ID")
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
	BASE_SITE = os.environ.get("BASE_SITE", "v2.kpslink.in")