# -*- coding: utf-8 -*-

"""
Created on Thu Feb 13 12:56:36 2020

@author: Saksham
"""

import time
from selenium import webdriver

#options = webdriver.ChromeOptions()
#options.add_argument("user-data-dir=C:\\Users\\Saksham\\AppData\\Local\\Google\\Chrome\\User Data\\Default")

#path_to_chromedriver = r'C:\Users\Saksham\Desktop\chromedriver.exe'
#driver = webdriver.Chrome(options = options, executable_path = path_to_chromedriver)
driver = webdriver.Chrome()

# Sensor API Service tab
driver.get('https://www.goodreads.com/')

'''
username = driver.find_element_by_id("login_id")
password = driver.find_element_by_id("login_password")

username.send_keys("my_username")
password.send_keys("my_password")

driver.find_element_by_name("submit").click()
'''
# first tab
driver.execute_script("window.open('about:blank', 'tab2');")
driver.switch_to.window("tab2")
driver.get('https://www.cricbuzz.com/')

# second tab
driver.execute_script("window.open('about:blank', 'tab3');")
driver.switch_to.window("tab3")
driver.get('https://www.google.com/')

# third tab
driver.execute_script("window.open('about:blank', 'tab4');")
driver.switch_to.window("tab4")
driver.get('https://stackoverflow.com/questions')

// main code
while True:
    Windows = driver.window_handles
    for window in Windows:
        driver.switch_to.window(window)
        time.sleep(5)
