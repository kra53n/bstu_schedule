TOOLS = (
    # {
    #     "name": "chrome",
    #     "urls": {
    #         "win32":   "",
    #         "win64":   "",
    #         "linux32": "",
    #         "linux64": "",
    #         "macos":   "",
    #     },
    # },
    {
        "name": "edge",
        "urls": {
            "win32":   "https://msedgedriver.azureedge.net/96.0.1054.62/edgedriver_win32.zip",
            "win64":   "https://msedgedriver.azureedge.net/96.0.1054.62/edgedriver_win64.zip",
            "linux32": "",
            "linux64": "https://msedgedriver.azureedge.net/96.0.1054.62/edgedriver_linux64.zip",
            "macos":   "https://msedgedriver.azureedge.net/96.0.1054.62/edgedriver_mac64.zip",
        },
    },
    {
        "name": "Firefox",
        "urls": {
            "win32":   "https://github.com/mozilla/geckodriver/releases/download/v0.30.0/geckodriver-v0.30.0-win32.zip",
            "win64":   "https://github.com/mozilla/geckodriver/releases/download/v0.30.0/geckodriver-v0.30.0-win64.zip",
            "linux32": "https://github.com/mozilla/geckodriver/releases/download/v0.30.0/geckodriver-v0.30.0-linux32.tar.gz",
            "linux64": "https://github.com/mozilla/geckodriver/releases/download/v0.30.0/geckodriver-v0.30.0-linux64.tar.gz",
            "macos":   "https://github.com/mozilla/geckodriver/releases/download/v0.30.0/geckodriver-v0.30.0-macos.tar.gz",
        },
    },
    # {
    #     "name": "ie",
    #     "urls": {
    #         "win32":   "",
    #         "win64":   "",
    #         "linux32": "",
    #         "linux64": "",
    #         "macos":   "",
    #     },
    # },
    {
        "name": "Opera",
        "urls": {
            "win32":   "https://github.com/operasoftware/operachromiumdriver/releases/download/v.96.0.4664.45/operadriver_win32.zip",
            "win64":   "https://github.com/operasoftware/operachromiumdriver/releases/download/v.96.0.4664.45/operadriver_win64.zip",
            "linux32": "",
            "linux64": "https://github.com/operasoftware/operachromiumdriver/releases/download/v.96.0.4664.45/operadriver_linux64.zip",
            "macos":   "https://github.com/operasoftware/operachromiumdriver/releases/download/v.96.0.4664.45/operadriver_mac64.zip",
        },
    },
    # {
    #     "name": "safari",
    #     "urls": {
    #         "win32":   "",
    #         "win64":   "",
    #         "linux32": "",
    #         "linux64": "",
    #         "macos":   "",
    #     },
    # },
)


TOOL_TO_USE = "Firefox"

URL = "https://www.tu-bryansk.ru/education/schedule"

CONFIG_FILE_NAME = "config"
CONFIG_NECESSARY_DATA = (
    "period",
    "faculty",
    "level",
    "group",
)

SLEEP_TIME = 0.2

ARGS = {
    "print config":  ("-p", "--print-config"),
    "change config": ("-c", "--change-config"),
    "change tool":   ("--change-tool"),
}
