import os
import configparser

HOMEPATH = os.path.dirname(__file__)[:-8]


# Setup requirements
def init_config():
    if not os.path.exists(HOMEPATH + "/config.ini"):
        print("No config.ini file found, creating default file.")
        config_file = configparser.ConfigParser()
        config_file["CompileSettings"] = {
            "remove_blank": "N",
            "remove_additional": "N",
            "remove_formula": "N",
            "download_directory": os.path.join(os.path.expanduser("~"), "Downloads")
        }

        with open(HOMEPATH + "/config.ini", 'w') as config_file_obj:
            config_file.write(config_file_obj)
            config_file_obj.flush()
            config_file_obj.close()

def fetch_from_config(item):
    init_config()
    config_file = configparser.ConfigParser()
    config_file.read(HOMEPATH + "/config.ini")
    return config_file.get("CompileSettings", item)

def save_to_config(item, value):
    init_config()
    config_file = configparser.ConfigParser()
    config_file.read(HOMEPATH + "/config.ini")
    config_file["CompileSettings"][item] = value
    with open(HOMEPATH + "/config.ini", 'w') as config_file_obj:
        config_file.write(config_file_obj)
        config_file_obj.flush()
        config_file_obj.close()

