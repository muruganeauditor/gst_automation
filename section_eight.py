import string
import sys
import requests
import datetime

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import section_one
from section_one import printMessage
from os.path import basename

basefilename = basename(__file__)+' '
getframe = sys._getframe

def NewEighthSection(browser, userData):
    try:
        printMessage('New Eighth form submission entry', basefilename + str(getframe().f_lineno), 0)

        browser.implicitly_wait(20)
        browser.save_screenshot('steps/eight-sectionnew-start.png')
        elementbs = WebDriverWait(browser, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Save & Continue')]"))
        )

        browser.implicitly_wait(30)
        elementSubmit = browser.find_element(By.XPATH, "//*[contains(text(), 'Save & Continue')]")
        printMessage(elementSubmit.get_attribute('type'), basefilename + str(getframe().f_lineno), 0)

        browser.execute_script("arguments[0].scrollIntoView(true);", elementSubmit)

        browser.execute_script("arguments[0].click();", elementSubmit)
    except Exception as e:
        browser.save_screenshot("8-exiterror41.png")
        printMessage(str(e), basefilename + str(getframe().f_lineno), 1)

def EditEighthSection(browser, userData):
    try:
        printMessage('Edit Eighth form submission entry', basefilename + str(getframe().f_lineno), 0)

        browser.implicitly_wait(20)
        browser.save_screenshot('eight-sectionedit-start.png')
        elementbs = WebDriverWait(browser, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Save & Continue')]"))
        )

        browser.implicitly_wait(30)
        elementSubmit = browser.find_element(By.XPATH, "//*[contains(text(), 'Save & Continue')]")
        printMessage(elementSubmit.get_attribute('type'), basefilename + str(getframe().f_lineno), 0)

        browser.execute_script("arguments[0].scrollIntoView(true);", elementSubmit)

        browser.execute_script("arguments[0].click();", elementSubmit)
    except Exception as e:
        browser.save_screenshot("8-exiterror62.png")
        printMessage(str(e), basefilename + str(getframe().f_lineno), 1)
