AVAILABLE_TOOLS = (
    "Chrome",
    "Edge",
    "Firefox",
    "Ie",
    "Opera",
    "PhantomJS",
    "Remote",
    "Safari",
    "WebKitGTK",
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
    "print config": ("-p", "--print-config"),
    "change config": ("-c", "--change-config"),
    "change tool": ("--change-tool"),
}
