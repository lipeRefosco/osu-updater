import os
from time import sleep
from requests import request
from version_handler import *

# URLs
URL_OSU_REPOSITORY = "https://api.github.com/repos/ppy/osu/releases/latest"
# URL_OSU_REPOSITORY = "http://localhost:8000"
URL_OSU_DOWNLOAD = "https://github.com/ppy/osu/releases/latest/download/osu.AppImage"

# Config
CONFIG_FOLDER = os.path.expanduser('~') + "/Games/osuLazer/"
CONFIG_FILE = "config.json"

# Game file definition
GAME_FILE = "osu.AppImage"

def main():
    is_installed = install()

    if is_installed:
        run()

def run():
    local_file = open(CONFIG_FOLDER + CONFIG_FILE)
    local_file = eval(local_file.read())

    while 1:
        # get infos about new version
        latest_version = request("get", URL_OSU_REPOSITORY).json()
        
        if local_file["id"] != latest_version["id"]:
            game_saved = get_new_version(
                url=URL_OSU_DOWNLOAD,
                path=CONFIG_FOLDER + GAME_FILE
            )
            if game_saved:
                save_infos(
                    file_path=CONFIG_FOLDER + CONFIG_FILE,
                    id=latest_version["id"]
                )
        
        sleep(60 * local_file["timer"]) # 60 seconds

def install() -> bool:
    directory_exist = os.path.exists(CONFIG_FOLDER)
    config_file_exist = os.path.exists(CONFIG_FOLDER + CONFIG_FILE)

    if directory_exist and config_file_exist:
        return True

    # Create default folder
    if not directory_exist:
        try:
            os.mkdir(CONFIG_FOLDER)

        except:
            print("Can't create a config folder")
            return False

    # Save default information file
    infos_saved = save_infos(CONFIG_FOLDER + CONFIG_FILE)
    
    if infos_saved:
        return True
    else:
        print("Can't install application!")
        return False


if __name__ == "__main__":
    main()
