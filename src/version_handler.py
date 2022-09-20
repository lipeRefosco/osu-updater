from datetime import datetime
from requests import request

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
        file.write(
            str(infos)
        )
        return True
    except Exception as e:
        print("Was't possible to save informations!")
        print(e)
        return False

def get_new_version(url : str, path: str) -> bool:
    print("Downloading... " + url)
    try:
        request_binary = request("get", url).content
        saved = save_download(path, request_binary)
        
        if saved:
            return True
        else:
            return False
        
    except Exception as e:
        print("Download Error!")
        print(e)
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
        print(f"Can't save downloaded file!")
        print(e)
        return False

def has_update(config_file: dict, request_infos: dict) -> bool:
    return True if config_file["id"] != request_infos["id"] else False
