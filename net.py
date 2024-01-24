# -*- encoding: utf-8 -*-
"""
@Modify Time          @Author      @Version    @Description
--------------      -----------    --------    ------------
2023/3/13 14:43     chuxiaodong      1.0           None
"""

import sys
import os
import threading
from time import sleep
from random import choice
from subprocess import CREATE_NO_WINDOW
import win32api
import win32con
from selenium import webdriver
from pythonping import ping
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from config import *


driver_path = os.path.dirname(__file__)+"/chromedriver.exe"
url = "http://10.254.7.4"
log_out_url = "http://10.254.7.4:801/eportal/portal/logout"
looptime = 30
name_path = "//*[@id=\"edit_body\"]/div[3]/div[1]/div/div[2]/div[1]/div/form/input[3]"
password_path = "//*[@id=\"edit_body\"]/div[3]/div[1]/div/div[2]/div[1]/div/form/input[4]"
click_path = "//*[@id=\"edit_body\"]/div[3]/div[1]/div/div[2]/div[1]/div/form/input[2]"
log_out_path = "//*[@id=\"edit_body\"]/div[2]/div[2]/form/input"


def get_driver():
    options = Options()
    service = Service(driver_path)
    service.creation_flags = CREATE_NO_WINDOW
    options.add_argument('--disable-extensions')
    options.add_argument("--disable-gpu")
    options.add_argument("--headless")
    options.add_argument('--blink-settings=imagesEnabled=false')
    driver = webdriver.Chrome(options=options, service=service)
    driver.implicitly_wait(5)
    return driver


def run(driver: webdriver.Chrome):
    driver.get(url)
    try:
        driver.find_element(By.XPATH, name_path).send_keys(username)
        driver.find_element(By.XPATH, password_path).send_keys(password)
        driver.find_element(By.XPATH, click_path).click()
    except:
        driver.find_element(By.XPATH, log_out_path)


def loop_check(driver):
    try:
        print("连接成功")
        while True:
            res = ping(choice(tests), count=1)
            if not res.success():
                break
            sleep(looptime)
    finally:
        threading.Thread(target=show, args=("断开重试",)).start()
        driver.get(log_out_url)


def show(s):
    win32api.MessageBox(0, s, "提醒", win32con.MB_OK)


chromedriver = get_driver()
try:
    while True:
        run(chromedriver)
        sleep(1)
        loop_check(chromedriver)
        sleep(3)
        chromedriver.close()
        sleep(2)
        chromedriver = get_driver()
except:
    threading.Thread(target=show, args=("连接断开\n",)).start()
    chromedriver.get(log_out_url)
    chromedriver.close()
finally:
    sleep(1)
    sys.exit(0)
