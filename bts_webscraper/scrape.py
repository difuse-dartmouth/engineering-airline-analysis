# date: 17 may 2023
# author: bendlev
# purpose: scrape website for BTS data

# import webdriving modules
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from tkinter import *
from tkinter.ttk import *

# import other modules
from time import sleep
import re
import os

# get screen height-width
root = Tk()
height = root.winfo_screenheight()
width = root.winfo_screenwidth()

# configure chrome options for webdriver
options = Options()
options.binary_location = r"bts_webscraper\internals\chrome.exe"
options.add_argument("--ignore-certificate-errors")
s = Service("bts_webscraper\webdriver\chromedriver_win32\chromedriver.exe")

# initialize webdriver
driver = webdriver.Chrome(service=s, options=options)

# do stuff

# driver.get(URL)
# driver.sleep(5)

# clean up after yourself

# driver.quit()