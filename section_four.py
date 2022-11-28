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

basefilename = basename(__file__) + ' '
getframe = sys._getframe


def NewFourthSection(browser, userData):
    try:
        printMessage("fourth form submission enters", basefilename + str(getframe().f_lineno), 0)
        browser.implicitly_wait(10)

        formElement = WebDriverWait(browser, 100).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Save & Continue')]"))
        )
        browser.save_screenshot('steps/four-sectionnew-end.png')
        elementbs = WebDriverWait(browser, 100).until(
            EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Save & Continue')]"))
        )

        browser.implicitly_wait(10)
        printMessage(elementbs.get_attribute('type'), basefilename + str(getframe().f_lineno), 0)
        browser.execute_script("arguments[0].click();", elementbs)

    except Exception as e:
        browser.execute_script("alert('please complete third section')")
        browser.save_screenshot("4-fourerror532.png")
        printMessage(str(e), basefilename + str(getframe().f_lineno), 1)


def EditFourthSection(browser, userData):
    pass
