# -*- coding: utf-8 -*-

import time
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
#options.add_argument("user-data-dir=C:\\Users\\Saksham\\AppData\\Local\\Google\\Chrome\\User Data\\Default")

path_to_chromedriver = r'C:\Users\Saksham\Desktop\auto tab switch\chromedriver.exe'
driver = webdriver.Chrome(options = options, executable_path = path_to_chromedriver)

def startTab(tab, url):
    js = "window.open('about:blank', '" +tab+ "');"
    driver.execute_script(js)
    driver.switch_to.window(tab)
    driver.get(url)

# Sensor API Service tab
driver.get('https://www.google.com')
time.sleep(10)

'''
username = driver.find_element_by_id("login_id")
password = driver.find_element_by_id("login_password")

username.send_keys("my_username")
password.send_keys("my_password")

driver.find_element_by_name("submit").click()
'''

# Sensor Ingestion Service tab
startTab('tab2', 'https://stackoverflow.com/questions')

# Sensor Subscription Service tab
startTab('tab3', 'https://www.google.com/')

# Historic Ingestion Service tab
startTab('tab4', 'https://www.cricbuzz.com/')

while True:
    Windows = driver.window_handles
    for window in Windows:
        driver.refresh()
        driver.switch_to.window(window)
        time.sleep(15)
