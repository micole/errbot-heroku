import logging
import os

# This is a minimal configuration to get you started with the Text mode.
# If you want to connect Errbot to chat services, checkout
# the options in the more complete config-template.py from here:
# https://raw.githubusercontent.com/errbotio/errbot/master/errbot/config-template.py

BACKEND = "SlackV3"  # Errbot will start in text mode (console only mode) and will answer commands from there.

os.mkdir('/tmp/data')
BOT_DATA_DIR = r"/tmp/data"
BOT_EXTRA_PLUGIN_DIR = r"/app/errbot-discord/plugins"

BOT_LOG_FILE = r"/app/errbot-discord/errbot.log"
BOT_LOG_LEVEL = logging.INFO

BOT_EXTRA_BACKEND_DIR = "/app/errbot-discord/err-backend-slackv3"

BOT_IDENTITY = {
    'token': os.getenv('TOKEN'),
    'signing_secret': os.getenv('SIGNING_SECRET'),
    'app_token': os.getenv('APP_TOKEN')
}

BOT_ADMINS = (
    "@micole.3",
)  # Don't leave this as "@CHANGE_ME" if you connect your errbot to a chat system!!
