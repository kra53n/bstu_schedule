from os import walk
import os.path

import yaml

from bstu_schedule.constants import (
    CONFIG_FILE_NAME,
    CONFIG_NECESSARY_DATA,
)


path_dir = __file__[:-(len(__name__) + len(".py"))]
config_filename = CONFIG_FILE_NAME + ".yaml"


def check_existing_config():
    return True if config_filename in tuple(walk(path_dir))[0][2] else False

def create_config_file():
    with open(os.path.join(path_dir, config_filename), "a") as f:
        pass

def file_content() -> dict:
    with open(os.path.join(path_dir, config_filename), "r") as f:
        return yaml.safe_load("".join(f.readlines()))

def return_skiped_necessary_data():
    f_content = file_content()
    if f_content == None:
        return CONFIG_NECESSARY_DATA

    f_content = f_content.keys()
    return [data for data in CONFIG_NECESSARY_DATA
            if data not in f_content]

def dump_data(data):
    with open(os.path.join(path_dir, config_filename), "w") as f:
        f.writelines(yaml.dump(data))
