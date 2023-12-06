from selenium import webdriver
from selenium.webdriver import ChromeOptions

actual_res = {
    "width" : 390,
    "height" : 844,
    "device" : "Iphone-12-Pro"
}

options = ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

driver.get("http://hotel-v3.progmasters.hu/")

res_tuple = (actual_res["width"], actual_res["height"])

tuples = [res_tuple, res_tuple[::-1]]

landscape = False

for current_width, current_height in tuples:
    driver.set_window_size(current_width, current_height)
    height_of_page = driver.execute_script("return $(document).height()")

    i = 1

    while current_height * i < height_of_page + current_height:
        driver.save_screenshot(f"filename_{landscape * "landscape_"}{i}.png")
        driver.execute_script(f"window.scrollTo(0, {current_height * i})")
        i += 1

    landscape = not landscape

#driver.quit()
