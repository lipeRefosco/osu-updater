import os
from time import sleep
from requests import request

# Program
from version_handler import *
from messages import MESSAGES
from definitions import *
from desktopfile import *

def main():
    is_installed = install()

    if is_installed:
        run()

def run():
    local_file = get_local_infos(CONFIG_FOLDER + CONFIG_FILE)

    # get infos about new version
    latest_version = request("get", URL_OSU_REPOSITORY).json()
    
    if has_update(local_file, latest_version):
        
        send_notification(MESSAGES["have_update"])
        game_saved = get_new_version(URL_OSU_DOWNLOAD, CONFIG_FOLDER + GAME_FILE)

        if game_saved:
            save_infos(CONFIG_FOLDER + CONFIG_FILE, latest_version["id"])
    
    sleep(60 * local_file["timer"]) # 60 seconds
    run()

def install() -> bool:
    directory_exist = os.path.exists(CONFIG_FOLDER)
    config_file_exist = os.path.exists(CONFIG_FOLDER + CONFIG_FILE)

    if directory_exist and config_file_exist:
        return True

    # Create default folder
    if not directory_exist:
        try:
            os.mkdir(GAMES_FOLDER)
            os.mkdir(CONFIG_FOLDER)

        except Exception as e:
            send_notification(MESSAGES["fails"]["mkdir"])
            logging.exception(str(e))
            return False

    # Save default information file
    infos_saved = save_infos(CONFIG_FOLDER + CONFIG_FILE)
    desktop_file_created = create_desktop_file(CONFIG_FOLDER + DESKTOP_FILE, DESKTOP_FILE)
    
    if not infos_saved and not desktop_file_created:
        send_notification(MESSAGES["fails"]["install"])
        return False
    
    send_notification(MESSAGES["instalation_finished"])
    return True


if __name__ == "__main__":
    main()
