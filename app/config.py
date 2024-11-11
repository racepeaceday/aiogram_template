from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')

BOT_TOKEN = config.get('bot', 'BOT_TOKEN')
ADMIN = config.get('chat', 'ADMIN')