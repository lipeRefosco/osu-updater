import os

# URLs
URL_OSU_REPOSITORY = "https://api.github.com/repos/ppy/osu/releases/latest"
# URL_OSU_REPOSITORY = "http://localhost:8000"
URL_OSU_DOWNLOAD = "https://github.com/ppy/osu/releases/latest/download/osu.AppImage"

# Folders
USER_FOLDER = os.path.expanduser("~")
GAMES_FOLDER = USER_FOLDER + "/Games/"
CONFIG_FOLDER = USER_FOLDER + "/Games/osuLazer/"

# Files
CONFIG_FILE = "config.json"
GAME_FILE = "osu.AppImage"