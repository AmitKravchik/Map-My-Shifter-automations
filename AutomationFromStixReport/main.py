from selenium import webdriver
import json
from pathlib import Path

# change to your local chrome driver path
DRIVER_PATH = 'C:/Users/amita/Downloads/chromedriver_win32/chromedriver.exe'

# change to your local stix shifter modules directory
BASE_PATH = "C:/Users/amita/Desktop/IBM/stix-shifter-develop/stix-shifter-develop/stix_shifter_modules"

# change to your local outpus path
OUTPUT_FILE_PATH = "results.json"

MODULE_JSON_SUBDIR = "stix_translation/json"
FILE_INDICATOR = "from_stix_map"
FILE_EXTENSION = ".json"
EXISTS_LABEL_EXTENSION = '9XdXe'
NOT_EXISTS_LABEL_EXTENSION = 'o-gXh'


def iterate_directory(path):
    dict = {}
    directory = Path(path)
    for module_path in directory.glob('*'):
        module_name = module_path.name
        # print (module_name)

        if module_path.is_dir():
            dict[module_name] = get_result(module_name)

    for k in list(dict.keys()):
        if len(dict[k]) == 0:
            del dict[k]

    return dict

def get_result(module_name):
    files_in_module_dict = {}
    file_list = list((Path(BASE_PATH).joinpath(module_name,MODULE_JSON_SUBDIR)).glob(f"*{FILE_INDICATOR}*{FILE_EXTENSION}"))
    for file in file_list:
        files_in_module_dict[file.name] = upload_file(file)
    return files_in_module_dict


def upload_file(path):
    driver.find_element_by_css_selector('input.bx--visually-hidden').send_keys(str(path))
    return open_lists()

def open_lists():
    resDict = {}
    li_accordion_items = driver.find_elements_by_xpath("//li[contains(@class,'bx--accordion__item')]")
    for li_item in li_accordion_items:
        button_name = (li_item.find_element_by_xpath("./button[contains(@class,'bx--accordion__heading')]").text).split(" ")[0]
        accordion_item = li_item.find_element_by_xpath("./div[contains(@id,'accordion-item-')]")
        existsFields = list(map(lambda i: i.get_attribute('innerHTML').strip(), accordion_item.
                                find_elements_by_xpath(f"./div[contains(@class,'{EXISTS_LABEL_EXTENSION}')]")))
        notExistsFields = list(map(lambda i: i.get_attribute('innerHTML').strip(), accordion_item.
                                   find_elements_by_xpath(f"./div[contains(@class,'{NOT_EXISTS_LABEL_EXTENSION}')]")))
        resDict[button_name] = {"existingFields": existsFields,"notExistingFields": notExistsFields}

    return resDict



driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get('https://ibm.github.io/map-my-shifter/#/from_stix')
driver.maximize_window()

resDict = iterate_directory(BASE_PATH)

with open(OUTPUT_FILE_PATH, "w") as f:
    json.dump(resDict, f)




