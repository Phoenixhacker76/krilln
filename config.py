# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

import os
import re
from os import environ, getenv

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

class Config(object):
    # Bot Information 
    TECH_VJ_BOT_TOKEN = os.environ.get("TECH_VJ_BOT_TOKEN", "6737660591:AAEDC_K7qdha0hvF2UnR8L1pxd6Cx8sTg3w")
    TECH_VJ_BOT_USERNAME = os.environ.get("TECH_VJ_BOT_USERNAME", "Brookv2_probot") # Bot username without @.
    
    # The Telegram API things
    TECH_VJ_API_ID = int(os.environ.get("TECH_VJ_API_ID", "21366247"))
    TECH_VJ_API_HASH = os.environ.get("TECH_VJ_API_HASH", "1d6666d32848a6878c191167a491205d")
    
    # the download location, where the HTTP Server runs
    TECH_VJ_DOWNLOAD_LOCATION = "./DOWNLOADS"
    
    # Telegram maximum file upload size
    TECH_VJ_MAX_FILE_SIZE = 50000000
    TECH_VJ_TG_MAX_FILE_SIZE = 4194304000 #2097152000
    TECH_VJ_FREE_USER_MAX_FILE_SIZE = 50000000
    
    # chunk size that should be used with requests
    TECH_VJ_CHUNK_SIZE = int(128)
    # default thumbnail to be used in the videos
    
    # proxy for accessing youtube-dl in GeoRestricted Areas
    # Get your own proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    TECH_VJ_HTTP_PROXY = ""
    
    # maximum message length in Telegram
    TECH_VJ_MAX_MESSAGE_LENGTH = 4096
    
    # set timeout for subprocess
    TECH_VJ_PROCESS_MAX_TIMEOUT = 3600
    
    # your telegram account id
    TECH_VJ_OWNER_ID = int(os.environ.get("TECH_VJ_OWNER_ID", " 1425888381")) 
    TECH_VJ_SESSION_NAME = "VJ-URL-UPLOADER-BOT"
    
    # database uri (mongodb)
    TECH_VJ_DATABASE_URL = os.environ.get("TECH_VJ_DATABASE_URL", "mongodb+srv://brookv2:brookv2@cluster0.k4imete.mongodb.net/?retryWrites=true&w=majority")
    TECH_VJ_MAX_RESULTS = "50"

    # channel information
    TECH_VJ_LOG_CHANNEL = int(os.environ.get("TECH_VJ_LOG_CHANNEL", "-1001684503916")) # your log channel id and make bot admin in log channel with full right 
    
    # if you want force subscribe then give your channel id below else leave blank
    tech_vj_update_channel = environ.get('TECH_VJ_UPDATES_CHANNEL', '') # your update channel id and make bot admin in update channel with full right
    TECH_VJ_UPDATES_CHANNEL = int(tech_vj_update_channel) if tech_vj_update_channel and id_pattern.search(tech_vj_update_channel) else None  
    
    # Url Shortner Information 
    TECH_VJ = bool(environ.get('TECH_VJ', True)) # Set False If you want shortlink off else True
    TECH_VJ_URL = environ.get('TECH_VJ_URL', 'gplinks.com') # your shortlink url domain or url without https://
    TECH_VJ_API = environ.get('TECH_VJ_API', 'f6ba197f379820db5a0fb01e99e7530c1a3b7836') # your url shortner api
    TECH_VJ_TUTORIAL = os.environ.get("TECH_VJ_TUTORIAL", "https://t.me/Hisoka_probot?start=Z2V0LTE1MDMwMzg2MjM5ODYw")


# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01
