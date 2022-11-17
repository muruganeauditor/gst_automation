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

def NewThirdSection(browser):
    try:
        printMessage("New Third form enters here", basefilename + str(getframe().f_lineno), 0)

        browser.implicitly_wait(20)
        primElement = WebDriverWait(browser, 400).until(
            EC.presence_of_element_located((By.ID, "auth_prim"))
        )
        printMessage(primElement.get_attribute('checked'), basefilename + str(getframe().f_lineno), 0)

        if primElement.get_attribute('checked') is None:
            element = browser.find_element(By.ID, "auth_prim")
            browser.execute_script("arguments[0].scrollIntoView(true);", element)

            browser.execute_script("arguments[0].click();", element)

    except Exception as e:
        browser.save_screenshot("3-primerror40.png")
        printMessage(str(e), basefilename + str(getframe().f_lineno), 1)

    try:

        elementpd = browser.find_element(By.ID, "as_locality")
        browser.execute_script("arguments[0].scrollIntoView(true);", elementpd)
        browser.implicitly_wait(5)
        browser.save_screenshot("3-primerror44.png")
        localityElement = WebDriverWait(browser, 50).until(
            EC.presence_of_element_located((By.ID, "as_locality"))
        )
        pd_locality = localityElement.get_attribute('value')
        printMessage(pd_locality, basefilename + str(getframe().f_lineno), 0)
        time.sleep(1)
    except Exception as e:
        pd_locality = ''
        browser.save_screenshot("3-localityerror.png")
        printMessage(str(e), basefilename + str(getframe().f_lineno), 1)

    try:
        printMessage('Third form submission started', basefilename + str(getframe().f_lineno), 0)

        browser.implicitly_wait(20)

        elementbs = WebDriverWait(browser, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Save & Continue')]"))
        )

        browser.implicitly_wait(30)
        elementSubmit = browser.find_element(By.XPATH, "//*[contains(text(), 'Save & Continue')]")
        printMessage(elementSubmit.get_attribute('type'), basefilename + str(getframe().f_lineno), 0)

        browser.execute_script("arguments[0].scrollIntoView(true);", elementSubmit)

        browser.execute_script("arguments[0].click();", elementSubmit)
    except Exception as e:
        browser.save_screenshot("3-exiterror60.png")
        printMessage(str(e), basefilename + str(getframe().f_lineno), 1)

    try:
        if pd_locality == '':
            browser.save_screenshot('3-alert.png')
            element = WebDriverWait(browser, 200).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="confirmDlg"]/div/div/div[2]/a[1]'))
            )
            element.click()
    except Exception as e:
        browser.save_screenshot('3-alerterror.png')
        printMessage(str(e), basefilename + str(getframe().f_lineno), 1)

def EditThirdSection(browser):
    try:
        printMessage('Edit Third form submission entry', basefilename + str(getframe().f_lineno), 0)

        browser.implicitly_wait(20)

        elementbs = WebDriverWait(browser, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Save & Continue')]"))
        )

        browser.implicitly_wait(30)
        elementSubmit = browser.find_element(By.XPATH, "//*[contains(text(), 'Save & Continue')]")
        printMessage(elementSubmit.get_attribute('type'), basefilename + str(getframe().f_lineno), 0)

        browser.execute_script("arguments[0].scrollIntoView(true);", elementSubmit)

        browser.execute_script("arguments[0].click();", elementSubmit)
    except Exception as e:
        browser.save_screenshot("3-exiterror501.png")
        printMessage(str(e), basefilename + str(getframe().f_lineno), 1)

    try:
        localityElement = WebDriverWait(browser, 50).until(
            EC.presence_of_element_located((By.ID, "as_locality"))
        )
        pd_locality = localityElement.get_attribute('value')
        printMessage(pd_locality, basefilename + str(getframe().f_lineno), 0)
        time.sleep(1)
    except Exception as e:
        pd_locality = ''
        browser.save_screenshot("3-localityerror.png")
        printMessage(str(e), basefilename + str(getframe().f_lineno), 1)


    try:
        if pd_locality == '':
            browser.save_screenshot('3-alert.png')
            element = WebDriverWait(browser, 200).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="confirmDlg"]/div/div/div[2]/a[1]'))
            )
            element.click()
    except Exception as e:
        browser.save_screenshot('3-alerterror.png')
        printMessage(str(e), basefilename + str(getframe().f_lineno), 1)