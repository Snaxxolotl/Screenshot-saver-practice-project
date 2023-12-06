import os
from selenium import webdriver
from selenium.webdriver import ChromeOptions
# from selenium.webdriver.common.by import By
import gettourl

for function_name in dir(gettourl):
    current_function = getattr(gettourl, function_name)
    print(function_name, callable(current_function))
    if callable(current_function):
        driver, dirname = current_function()

        resolutions = [
            {
                "width" : 390,
                "height" : 844,
                "device" : "Iphone_12_Pro"
            },
            {
                "width" : 768,
                "height" : 1024,
                "device" : "iPad_2_mini"
            },
        {
                "width" : 320,
                "height" : 480,
                "device" : "iPhone_3_4"
            },
        ]
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
                height_of_page = driver.execute_script("return $(document).height()")

                i = 1

                while current_height * i < height_of_page + current_height:
                    driver.save_screenshot(f"./{dirname}/{device_name}/filename_{landscape * "landscape_"}{i}.png")
                    driver.execute_script(f"window.scrollTo(0, {current_height * i})")
                    i += 1

                landscape = not landscape

#driver.quit()
