# ZeldrisRobot
# Copyright (C) 2017-2019, Paul Larsen
# Copyright (C) 2022, IDNCoderX Team, <https://github.com/IDN-C-X/ZeldrisRobot>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.


if not __name__.endswith("sample_config"):
    import sys

    print(
        "The README is there to be read. Extend this sample config to a config file, don't just rename and change "
        "values here. Doing that WILL backfire on you.\nBot quitting.",
        file=sys.stderr,
    )
    sys.exit(1)


# Create a new config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True

    # REQUIRED
    TOKEN = "7204983300:AAGFwLAEIy8_HdVUSKxD4EIdcAR5bVnHwQo"  # Take from @BotFather
    OWNER_ID = (
        "5536168611"  # If you dont know, run the bot and do /id in your private chat with it
    )
    OWNER_USERNAME = "DARKCURSED0"
    API_HASH = None  # for purge stuffs
    API_ID = None

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = "postgres://avnadmin:AVNS_gwvtPgMcQ7IX0qwaCG9@freedb-mayrice01.i.aivencloud.com:14358/defaultdb?sslmode=require"  # needed for any database modules
    MESSAGE_DUMP = None # needed to make sure 'save from' messages persist
    REDIS_URL = "redis://something@nothing/anything:10002"  # needed for afk module, get from redislab
    LOAD = []
    NO_LOAD = ['translation']
    WEBHOOK = False
    URL = None
    MONGO_URI = "mongodb+srv://Dark123:Dark123@cluster0.jsapbqx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    MONGO_PORT = 27017  # leave it as it is
    MONGO_DB = "Cluster0"

    # OPTIONAL
    DEV_USERS = (
        []
    )  # List of id's (not usernames) for users which have sudo access to the bot.
    SUPPORT_USERS = (
        []
    )  # List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    WHITELIST_USERS = (
        []
    )  # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    WHITELIST_CHATS = []
    BLACKLIST_CHATS = []
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = False  # Whether or not you should delete "blue text must click" commands
    STRICT_GBAN = True
    WORKERS = 8  # Number of subthreads to use. This is the recommended amount - see for yourself what works best!
    BAN_STICKER = None  # banhammer marie sticker
    ALLOW_EXCL = False  # DEPRECATED, USE BELOW INSTEAD! Allow ! commands as well as /
    CUSTOM_CMD = False  # Set to ('/', '!') or whatever to enable it, like ALLOW_EXCL but with more custom handler!
    API_OPENWEATHER = None  # OpenWeather API
    SPAMWATCH_API = None  # Your SpamWatch token
    WALL_API = None
    SPAMMERS = None


class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True
