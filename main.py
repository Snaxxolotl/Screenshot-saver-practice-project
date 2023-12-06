import os
from selenium import webdriver
from selenium.webdriver import ChromeOptions
# from selenium.webdriver.common.by import By
import json

import gettourl

json_file = open('res_list.json')
resolutions = json.load(json_file)

for function_name in dir(gettourl):
    current_function = getattr(gettourl, function_name)
    if callable(current_function):
        driver, dirname = current_function()

        for actual_res in resolutions:
            res_tuple = (actual_res["width"], actual_res["height"])
            tuples = [res_tuple, res_tuple[::-1]]
            device_name = actual_res["device"]
            current_path = os.getcwd()
            path = os.path.join(current_path, dirname, device_name)
            os.makedirs(path)

            landscape = False

            for current_width, current_height in tuples:
                driver.set_window_size(current_width, current_height)
                driver.execute_script(f"window.scrollTo(0,0)")
                height_of_page = driver.execute_script("return $(document).height()")

                i = 1

                while current_height * i < height_of_page + current_height:
                    driver.save_screenshot(f"./{dirname}/{device_name}/filename_{landscape * 'landscape_'}{i}.png")
                    driver.execute_script(f"window.scrollTo(0, {current_height * i})")
                    i += 1

                landscape = not landscape

driver.quit()
