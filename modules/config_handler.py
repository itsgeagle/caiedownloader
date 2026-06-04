import os
import configparser

HOMEPATH = os.path.join(os.path.expanduser("~"), ".caiedownloader")


# Setup requirements
def init_config():
    if not os.path.exists(HOMEPATH):
        os.makedirs(HOMEPATH)
    if not os.path.exists(os.path.join(HOMEPATH, "config.ini")):
        print("No config.ini file found, creating default file.")
        config_file = configparser.ConfigParser()
        config_file["CompileSettings"] = {
            "remove_blank": "N",
            "remove_additional": "N",
            "remove_formula": "N",
            "download_directory": os.path.join(os.path.expanduser("~"), "Downloads")
        }

        with open(os.path.join(HOMEPATH, "config.ini"), 'w') as config_file_obj:
            config_file.write(config_file_obj)
            config_file_obj.flush()
            config_file_obj.close()
    config = configparser.ConfigParser()
    config.read(os.path.join(HOMEPATH, "config.ini"))

    try: _ = config["CompileSettings"]["remove_blank"]
    except KeyError: config["CompileSettings"]["remove_blank"] = "N"

    try: _ = config["CompileSettings"]["remove_additional"]
    except KeyError: config["CompileSettings"]["remove_additional"] = "N"

    try: _ = config["CompileSettings"]["remove_formula"]
    except KeyError: config["CompileSettings"]["remove_formula"] = "N"

    try: _ = config["CompileSettings"]["download_directory"]
    except KeyError: config["CompileSettings"]["download_directory"] = os.path.join(os.path.expanduser("~"), "Downloads")

    with open(os.path.join(HOMEPATH, "config.ini"), 'w') as config_file_obj:
        config.write(config_file_obj)
        config_file_obj.flush()
        config_file_obj.close()


def fetch_from_config(item):
    init_config()
    config_file = configparser.ConfigParser()
    config_file.read(os.path.join(HOMEPATH, "config.ini"))
    return config_file.get("CompileSettings", item)

def save_to_config(item, value):
    init_config()
    config_file = configparser.ConfigParser()
    config_file.read(os.path.join(HOMEPATH, "config.ini"))
    config_file["CompileSettings"][item] = value
    with open(os.path.join(HOMEPATH, "config.ini"), 'w') as config_file_obj:
        config_file.write(config_file_obj)
        config_file_obj.flush()
        config_file_obj.close()
