import os
import logging
from datetime import datetime
from requests import request
from messages import MESSAGES

def save_infos(
        file_path : str,
        id        : int = 0,
        timer_min : int = 20
    ) -> bool:

    infos = {
        "id" : id,
        "date": str(datetime.today()),
        "timer": timer_min
    }

    try:
        file = open(file_path, "w")
        file.write(str(infos))
        return True
    except Exception as e:
        send_notification(MESSAGES["fails"]["save_infos"])
        logging.exception(str(e))
        return False

def create_desktop_file(file_path: str, dektopfile: str) -> bool:
    try:
        desktop_file = open(file_path, "w")
        desktop_file.write(dektopfile)
        desktop_file.close()
        return desktop_file.closed
    except Exception as e:
        send_notification(MESSAGES["fails"]["desktop_file"])
        logging.exception(str(e))
        return False

def get_new_version(url: str, path: str) -> bool:

    send_notification(MESSAGES["downloading"] + url)

    try:
        request_binary = request("get", url).content
        is_saved = save_download(path, request_binary)
        return is_saved
        
    except Exception as e:
        send_notification(MESSAGES["fails"]["download"])
        logging.exception(str(e))
        return False

def save_download(path: str, file) -> bool:
    print(f"Saving download to {path}")
    try:
        final_file = open(path, "wb")
        final_file.write(file)
        final_file.close()
        print()
        return True
    except Exception as e:
        send_notification(MESSAGES["fails"]["save_file"])
        logging.exception(str(e))
        return False

def get_local_infos(config_file_path: str) -> dict:
    return eval(open(config_file_path).read())

def has_update(config_file: dict, request_infos: dict) -> bool:
    return True if config_file["id"] != request_infos["id"] else False

def send_notification(message: str):
    return os.system(f'notify-send "{message}"')
