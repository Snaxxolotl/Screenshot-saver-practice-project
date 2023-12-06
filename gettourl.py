# def create_driver():
#     import os
#     from selenium import webdriver
#     from selenium.webdriver import ChromeOptions
#     # from selenium.webdriver.common.by import By
#     options = ChromeOptions()
#     options.add_experimental_option("detach", True)
#     driver = webdriver.Chrome(options=options)
#     return driver

def visit_mainpage():
    import os
    from selenium import webdriver
    from selenium.webdriver import ChromeOptions
    options = ChromeOptions()
    options.add_argument("--headless")
    options.add_experimental_option("detach", True)
    options.add_argument("--window-size=2560,1440")
    driver = webdriver.Chrome(options=options)
    driver.get('http://hotel-v3.progmasters.hu/')
    return driver, "mainpage"

def register_page():
    import os
    from selenium import webdriver
    from selenium.webdriver import ChromeOptions
    from selenium.webdriver.common.by import By
    options = ChromeOptions()
    options.add_argument("--headless")
    options.add_experimental_option("detach", True)
    options.add_argument("--window-size=2560,1440")
    driver = webdriver.Chrome(options=options)
    driver.get('http://hotel-v3.progmasters.hu/')
    driver.find_element(By.ID, 'dropbar').click()
    driver.find_element(By.XPATH, '//a[text()="Vendég"]').click()
    return driver, "register"