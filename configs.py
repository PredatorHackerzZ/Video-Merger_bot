# (c) @AbirHasan2005 | @tellyfun4u

import os


class Config(object):
    API_ID = os.environ.get("API_ID")
    API_HASH = os.environ.get("API_HASH")
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    SESSION_NAME = os.environ.get("SESSION_NAME", "Video-Merger_Bot")
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL")
    LOG_CHANNEL = os.environ.get("LOG_CHANNEL")
    DOWN_PATH = os.environ.get("DOWN_PATH", "./downloads")
    TIME_GAP = int(os.environ.get("TIME_GAP", 5))
    MAX_VIDEOS = int(os.environ.get("MAX_VIDEOS", 5))
    MONGODB_URI = os.environ.get("MONGODB_URI")
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
    BOT_OWNER = int(os.environ.get("BOT_OWNER", 1445283714))

    START_TEXT = """
Hello! I am a video Merger Bot! By @tellyfun4u
This Bot can Merge Multiple Videos in One Video And Video Formats must to be same. 

Made by @tellyfun4u
"""
    CAPTION = "Video Merged by @{}\n\nMade by\n\n@tellyfun4u"
    PROGRESS = """
🛠Percentage : {0}%
✅Done: {1}
📡Total: {2}
🚀Speed: {3}/s
⏳ETA: {4}
"""
