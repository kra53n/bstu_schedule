from time import sleep
from sys import argv
from selenium import webdriver

import constants
import config
import web


BROWSERS = tuple(i["name"] for i in constants.TOOLS)


def make_choice(options: list, title: str) -> int:
    message = f"\n{title}\n"
    for option_num, name_option in enumerate(options):
        message += f"\t{option_num+1}. {name_option}\n"
    message += "\nChoose option: "

    while value := input(message):
        try:
            value = int(value)
            if not (value > 0 and value < len(options) + 1):
                continue
        except ValueError:
            continue
        return value - 1

def options_selector_elems(driver, option_name) -> list:
    return driver.find_element("id", option_name
        ).find_elements("tag name", "option")

def selector_options(driver, option_name) -> list:
    return [
        option.text for option
        in options_selector_elems(driver, option_name)
    ]

def choose_select_option(driver, selector: str, option: str):
    for elem in options_selector_elems(driver, selector):
        if elem.text == option:
            elem.click()
    sleep(constants.SLEEP_TIME)

def fill_necessary_data_to_config(driver, config_data: dict):
    for key in config.return_skiped_necessary_data():
        options = selector_options(driver, key)
        choice = make_choice(options, f"choose {key}".upper())
        choose_select_option(driver, key, options[choice])
        config_data[key] = options[choice]
    config.dump_data(config_data)

def create_config_if_not_exist():
    if not config.check_existing_config():
        config.create_config_file()

def dump_tool_to_config() -> str:
    choice = make_choice(BROWSERS, "choose tool".upper())
    tool_name = BROWSERS[choice]

    data = config.file_content()
    if data != None:
        data["tool"] = tool_name
    else:
        data = {"tool": tool_name}

    config.dump_data(data)
    return tool_name

def tool_in_config() -> str:
    create_config_if_not_exist()
    content = config.file_content()

    if content == None or "tool" not in content.keys() or \
        content["tool"] not in BROWSERS:
        tool_name = dump_tool_to_config()
    else:
        tool_name = content["tool"]

    web.set_driver(tool_name, config.path_dir)

    return tool_name

def process_args():
    args = argv[1:]
    isarg = lambda key: any(1 for arg in argv[1:] if arg in key)

    if isarg(constants.ARGS["print config"]):
        pass
    if isarg(constants.ARGS["change config"]):
        pass
    if isarg(constants.ARGS["change tool"]):
        pass

def init_driver(wdt_scr=720, hgt_scr=720):
    tool_name = tool_in_config()
    driver = eval(f"webdriver.{tool_name}()")
    driver.set_window_size(wdt_scr, hgt_scr)
    driver.get(constants.URL)
    return driver

def start_fill_in_browser(driver):
    create_config_if_not_exist()

    if len(config.return_skiped_necessary_data()) > 0:
        fill_necessary_data_to_config(driver, {})
    else:
        data = config.file_content()
        [choose_select_option(driver, selector, data[selector])
        for selector in constants.CONFIG_NECESSARY_DATA]

def main():
    driver = init_driver()
    process_args()
    start_fill_in_browser(driver)


if __name__ == "__main__":
    main()
