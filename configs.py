# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "22349465"))
    API_HASH = getenv("API_HASH", "3732e079c4125690226d8e7b4e028ca4")
    BOT_TOKEN = getenv("BOT_TOKEN", "7497272339:AAGy8TNhAEVsQ1V6P6wcAU3iBXgscCZXz7E")
    # Your Force Subscribe Channel Id Below 
    CHID = int(getenv("CHID", "-1002273359017")) # Make Bot Admin In This Channel
    # Admin Or Owner Id Below
    SUDO = list(map(int, getenv("SUDO", "5469498838").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://teekam9079:teekam@tjbots.oppxq.mongodb.net/?retryWrites=true&w=majority&appName=TJBOTS")
    
cfg = Config()

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
