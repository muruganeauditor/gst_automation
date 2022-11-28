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

def NewThirdSection(browser, userData):
    try:
        printMessage("New Third form enters here", basefilename + str(getframe().f_lineno), 0)

        browser.implicitly_wait(20)
        primElement = WebDriverWait(browser, 400).until(
            EC.presence_of_element_located((By.ID, "auth_prim"))
        )
        checkboxExists = 1
        printMessage('checkbox exists', basefilename + str(getframe().f_lineno), 0)
        browser.save_screenshot('steps/three-sectionnew-start.png')
    except Exception as e:
        checkboxExists = 0
        browser.save_screenshot("3-primerrorstatus.png")
        printMessage(str(e), basefilename + str(getframe().f_lineno), 1)

    if userData['constitution_business'] != 'PVT' or checkboxExists==1:
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
            browser.execute_script("alert('please complete second section')")
            browser.save_screenshot("3-primerror40.png")
            printMessage(str(e), basefilename + str(getframe().f_lineno), 1)

        if userData['constitution_business'] == 'PVT' or checkboxExists == 1:
            letterExists = 0
            try:
                element = WebDriverWait(browser, 40).until(
                    EC.element_to_be_clickable((By.XPATH, '//*[@id="newRegForm"]/div[2]/fieldset[2]/div/div[1]/div/div/div/ul/li[2]/div/button'))
                )
                letterExists = 1
            except Exception as e:
                browser.save_screenshot("3-submiterror67.png")
                printMessage(str(e), basefilename + str(getframe().f_lineno), 1)

            if letterExists==0:
                try:
                    sel = Select(browser.find_element("id", 'as_up_type'))
                    browser.implicitly_wait(10)
                    sel.select_by_value('LOAU')

                except Exception as e:
                    printMessage(str(e), basefilename + str(getframe().f_lineno), 1)

                try:
                    fileElement = WebDriverWait(browser, 200).until(
                        EC.presence_of_element_located((By.ID, "as_upload_sign"))
                    ).send_keys('C:\\Users\\Liva\\Desktop\\download.jpg')
                except Exception as e:
                    browser.save_screenshot("2-profile.png")
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

        if userData['constitution_business'] == 'PVT' and checkboxExists==0:
            elementbs = WebDriverWait(browser, 30).until(
                EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Save & Continue')]"))
            )

            browser.implicitly_wait(30)
            elementSubmit = browser.find_element(By.XPATH, "//*[contains(text(), 'Save & Continue')]")
        else:
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

    if userData['constitution_business']:
        browser.save_screenshot('steps/three-sectionnew-end.png')
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

def EditThirdSection(browser, userData):
    try:
        printMessage('Edit Third form submission entry', basefilename + str(getframe().f_lineno), 0)

        browser.implicitly_wait(20)
        browser.save_screenshot('steps/three-sectionedit-start.png')
        if userData['constitution_business'] == 'PVT':
            elementbs = WebDriverWait(browser, 30).until(
                EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Continue')]"))
            )

            browser.implicitly_wait(30)
            elementSubmit = browser.find_element(By.XPATH, "//*[contains(text(), 'Continue')]")
        else:
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

    if userData['constitution_business'] != 'PVT':
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
            browser.save_screenshot('steps/three-sectionedit-end.png')
        except Exception as e:
            browser.save_screenshot('3-alerterror.png')
            printMessage(str(e), basefilename + str(getframe().f_lineno), 1)