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
from colorama import Fore
import os
from os.path import basename

basefilename = basename(__file__)+' '
getframe = sys._getframe

def NewFirstSection(browser, userData):
    global datetime
    try:
        printMessage("Entering into New save and continue", basefilename+str(getframe().f_lineno), 0)

        elementPara = WebDriverWait(browser, 20).until(
            EC.presence_of_element_located((By.ID, "tnm"))
        ).send_keys(userData['trade_name'])
        # browser.find_element("id", "tnm").send_keys('Test trades')
    except Exception as e:
        browser.save_screenshot('1-trade_error.png')
        printMessage(str(e), basefilename + str(getframe().f_lineno), 1)

    try:
        sel = Select(browser.find_element("id", 'bd_ConstBuss'))
        browser.implicitly_wait(10)
        sel.select_by_value(userData['constitution_business'])

    except Exception as e:
        printMessage(str(e), basefilename + str(getframe().f_lineno), 1)

    try:
        sel = Select(browser.find_element("id", 'bd_rsl'))
        browser.implicitly_wait(10)
        sel.select_by_value(userData['registration_reason'])

    except Exception as e:
        printMessage(str(e), basefilename + str(getframe().f_lineno), 1)

    try:
        browser.implicitly_wait(20)
        element = browser.find_element(By.ID, "bd_cmbz")
        browser.execute_script("arguments[0].scrollIntoView(true);", element)
        printMessage("Date field located", basefilename + str(getframe().f_lineno), 0)
    except Exception as e:
        browser.save_screenshot('1-bderror.png')
        printMessage(str(e), basefilename + str(getframe().f_lineno), 1)

    format = '%Y-%m-%d'
    datetimenew = datetime.datetime.strptime(userData['business_date'], format)
    userData['business_date'] = datetimenew.date().strftime("%d%m%Y")

    try:
        WebDriverWait(browser, 250).until(
            EC.presence_of_element_located((By.ID, "bd_cmbz"))
        ).send_keys(userData['business_date'])
        dateElement = browser.find_element(By.ID, "bd_cmbz")
        dateExists = dateElement.get_attribute('value')
        printMessage('dob'+dateExists, basefilename + str(getframe().f_lineno), 0)
        if dateExists == '':
            dobElement = WebDriverWait(browser, 200).until(
                EC.presence_of_element_located((By.ID, "bd_cmbz"))
            ).send_keys(userData['business_date'])
            browser.find_element("id", "bd_cmbz").send_keys(userData['business_date'])
        printMessage("Date field filled", basefilename + str(getframe().f_lineno), 0)
    except Exception as e:
        browser.save_screenshot("1-date.png")
        printMessage(str(e), basefilename + str(getframe().f_lineno), 1)

    # try:
    #     fileElement = WebDriverWait(browser, 200).until(
    #         EC.presence_of_element_located((By.ID, "tr_upload"))
    #     ).send_keys('C:\\Users\\Murugan\\Desktop\\WhatsApp.jpeg')
    # except Exception as e:
    #     browser.save_screenshot("1-file.png")
    #     printMessage(str(e), basefilename + str(getframe().f_lineno), 1)

    # try:
    #     print("1 - entering into save and continue")
    #     browser.implicitly_wait(20)
    #
    #     element = WebDriverWait(browser, 30).until(
    #         EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Save & Continue')]"))
    #     )
    #
    #     print('1 - 145', element)
    #     browser.implicitly_wait(30)
    #     print('1 - 147', element.get_attribute('type'))
    #     print("1 - save and continue works")
    #     element.click()
    # except Exception as e:
    #     elementnew = WebDriverWait(browser, 30).until(
    #         EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Save & Continue')]"))
    #     )
    #
    #     elementnew.click()
    #     browser.save_screenshot("1-saveerror156.png")
    #     print('ex 1-157', str(e))

    try:
        printMessage("entering into first save and continue", basefilename + str(getframe().f_lineno), 0)

        browser.implicitly_wait(10)

        element = WebDriverWait(browser, 50).until(
            EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Save & Continue')]"))
        )

        # print(145, element)
        browser.implicitly_wait(30)
        printMessage(element.get_attribute('type'), basefilename + str(getframe().f_lineno), 0)
        element.click()

    except Exception as e:
        elementnew = WebDriverWait(browser, 40).until(
            EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Save & Continue')]"))
        )

        elementnew.click()
        browser.save_screenshot("1-saveerror156.png")
        printMessage(str(e), basefilename + str(getframe().f_lineno), 1)


def EditFirstSection(browser, userData):
    try:
        printMessage("entering into edit save and continue", basefilename+str(getframe().f_lineno), 0)
        # print("entering into edit save and continue")
        browser.implicitly_wait(20)

        element = WebDriverWait(browser, 100).until(
            EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Save & Continue')]"))
        )

        # print(145, element)
        browser.implicitly_wait(10)
        printMessage(element.get_attribute('type'), basefilename + str(getframe().f_lineno), 0)
        # element.click()
        browser.execute_script("arguments[0].click();", element)
        printMessage('save and continue works', basefilename + str(getframe().f_lineno), 0)
    except Exception as e:
        # elementnew = WebDriverWait(browser, 30).until(
        #     EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Save & Continue')]"))
        # )
        #
        # elementnew.click()
        browser.save_screenshot("1-saveerror156.png")
        printMessage(str(e), basefilename + str(getframe().f_lineno), 1)


def printMessage(message, lineno, type=0):
    if type==0:
        print('Info:', lineno, message, sep='/')
    else:
        print('Error:',lineno, message, sep='//')