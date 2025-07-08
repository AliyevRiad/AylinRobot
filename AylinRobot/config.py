# @AylinRobot
# Sahib @HuseynH
# Repo Açığdısa İcazəsis Götürmə Oğlum
# Reponu Satan Kodların Götürən Kimliyindən Aslı Olmayaraq Peysərdi

# @AylinRobot
# Sahib @HuseynH
# Repo Açığdısa İcazəsis Götürmə Oğlum

import os

class Config:

   API_ID = int(os.getenv("API_ID", "27804609"))
   API_HASH = os.getenv("API_HASH", "e27685923fc24e08591caff39e764bbd")
   BOT_TOKEN = os.getenv("BOT_TOKEN", "8178467532:AAHjiM50RTnd6TRqiSVcW045_x9ujm7XwTY")
   BOT_USERNAME = os.environ.get("BOT_USERNAME", "SevincRobot")
   BOT_NAME = os.environ.get("BOT_NAME", "Sevinc 🌹")   
   OWNER_ID = int(os.environ.get("OWNER_ID","7926847490"))
   OWNER_NAME = os.environ.get("OWNER_NAME", "AliyevRiad") 
   GONDERME_TURU = bool(os.environ.get("GONDERME_TURU", "False"))
   MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb+srv://TEAMBABY01:UTTAMRATHORE09@cluster0.vmjl9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
   LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002606202136"))
   PLAYLIST_NAME = os.environ.get("PLAYLIST_NAME", "Oa")
   PLAYLIST_ID = int(os.environ.get("PLAYLIST_ID", "-1002606202136"))
   BAN_GROUP = int(os.environ.get("BAN_GROUP", "-1002606202136"))
   HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", "HRKU-AAwNu2aaHv0TKXSUaUJ6gxk_XODl79TyKs0giLl-RsFQ_wx11gGHU63r")
   ALIVE_NAME = os.environ.get("ALIVE_NAME", "Riad")
   CHANNEL = os.environ.get("CHANNEL", "OaGroupSupport")
   SUPPORT = os.environ.get("SUPPORT", "OaGroupSupport")
   ALIVE_IMG = os.environ.get("ALIVE_IMG", "https://telegra.ph/file/f6c186e3c581a223856c4.mp4") 
   START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/b2c2ed59a89933a384ae3.jpg")
   COMMAND_PREFIXES = list(os.environ.get("COMMAND_PREFIXES", "/ ! .").split())
