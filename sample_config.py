import os

api_id = 29946578
api_hash = os.environ.get("API_HASH", "57e0b762f105ab1db072fabe4d65114b")
bot_token = os.environ.get("BOT_TOKEN")
auth_users = os.environ.get("AUTH_USERS", "7731407856")
sudo_users = [int(num) for num in auth_users.split(",")]
osowner_users = os.environ.get("OWNER_USERS", "7731407856")
owner_users = [int(num) for num in osowner_users.split(",")]
