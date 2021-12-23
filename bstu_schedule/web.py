from requests import get
from zipfile import ZipFile
from struct import calcsize
from sys import platform
from os import remove
import os.path

import bstu_schedule.constants as constants


def osname():
    if platform == "win32":
        return platform[:3] + str(calcsize("P") * 8)
    if platform == "linux":
        return platform + calcsize("P") * 8
    if platform == "darwin":
        return "macos"

def dl_driver(browser, path):
    for tool in constants.TOOLS:
        if tool["name"] == browser:
            with open(path, "wb") as f:
                f.writelines(get(tool["urls"][osname()]))
            break

def set_driver(browser, path):
    path = os.path.join(path, "driver")
    dl_driver(browser, path)
    with ZipFile(path, "r") as zip_obj:
        zip_obj.extractall()
    remove(path)
