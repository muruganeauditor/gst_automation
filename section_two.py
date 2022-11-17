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

def NewSecondSection(browser):
    try:
        printMessage("Entering into second new form", basefilename + str(getframe().f_lineno), 0)
        browser.implicitly_wait(10)

        elementPara = WebDriverWait(browser, 50).until(
            EC.presence_of_element_located((By.ID, "ffname"))
        )
        browser.execute_script("arguments[0].scrollIntoView(true);", elementPara)
        browser.save_screenshot('2-fatherfocus.png')
        fnameElement = WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.ID, "ffname"))
        ).send_keys('Palani')
    except Exception as e:
        browser.save_screenshot('2-fathererror.png')
        printMessage(str(e), basefilename + str(getframe().f_lineno), 1)

    try:
        browser.implicitly_wait(10)
        fnameElement = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, "pd_flname"))
        ).send_keys('Vediyappan')
    except Exception as e:
        browser.save_screenshot('2-fatherlerror.png')
        printMessage(str(e), basefilename + str(getframe().f_lineno), 1)

    try:
        browser.implicitly_wait(20)
        dobElementnew = WebDriverWait(browser, 200).until(
            EC.presence_of_element_located((By.ID, "dob"))
        )
        browser.execute_script("arguments[0].setAttribute('value',arguments[1])", dobElementnew, '10051990')

        # elementdob = WebDriverWait(browser, 20).until(
        #     EC.presence_of_element_located((By.ID, "dob"))
        # )
        dobElement = browser.find_element(By.ID, "dob")
        dobExists = dobElement.get_attribute('value')
        browser.implicitly_wait(20)
        browser.find_element("id", "dob").send_keys('')
        printMessage("dob"+dobExists, basefilename + str(getframe().f_lineno), 0)

        browser.save_screenshot("2-dob58.png")
        if dobExists=='' or dobExists=='DD/MM/YYYY':
            dobElement = WebDriverWait(browser, 200).until(
                EC.presence_of_element_located((By.ID, "dob"))
            ).send_keys('10051990')
            browser.save_screenshot("2-dobmpty57.png")

            browser.find_element("id", "dob").send_keys('10051990')
            printMessage(dobElement, basefilename + str(getframe().f_lineno), 0)

    except Exception as e:
        browser.save_screenshot("2-doberror.png")
        printMessage(str(e), basefilename + str(getframe().f_lineno), 1)

    try:
        mobileElement = WebDriverWait(browser, 50).until(
            EC.presence_of_element_located((By.ID, "mbno"))
        ).send_keys('9585393730')
    except Exception as e:
        browser.save_screenshot("2-mobileerror.png")
        printMessage(str(e), basefilename + str(getframe().f_lineno), 1)

    try:
        mobileElement = WebDriverWait(browser, 50).until(
            EC.presence_of_element_located((By.ID, "pd_email"))
        ).send_keys('muruganaccetcse@gmail.com')
    except Exception as e:
        browser.save_screenshot("2-emailerror.png")
        printMessage(str(e), basefilename + str(getframe().f_lineno), 1)

    try:
        browser.implicitly_wait(5)
        gender = 'Male'

        genderfield = browser.find_element(By.CSS_SELECTOR, '#radiomale')
        # print(gender, genderfield)
        browser.execute_script("arguments[0].click();", genderfield)
    except Exception as e:
        printMessage(str(e), basefilename + str(getframe().f_lineno), 1)

    try:
        desElement = WebDriverWait(browser, 50).until(
            EC.presence_of_element_located((By.ID, "dg"))
        ).send_keys('Proprietor')
    except Exception as e:
        browser.save_screenshot("2-proerror.png")
        printMessage(str(e), basefilename + str(getframe().f_lineno), 1)

    try:
        fileElement = WebDriverWait(browser, 200).until(
            EC.presence_of_element_located((By.ID, "pd_upload"))
        ).send_keys('C:\\Users\\Murugan\\Desktop\\download.jpg')
    except Exception as e:
        browser.save_screenshot("2-profile.png")
        printMessage(str(e), basefilename + str(getframe().f_lineno), 1)

    try:
        browser.implicitly_wait(5)

        element = browser.find_element(By.ID, "pri_auth")
        browser.execute_script("arguments[0].scrollIntoView(true);", element)

        browser.execute_script("arguments[0].click();", element)

        # element = WebDriverWait(browser, 40).until(
        #     EC.element_to_be_clickable((By.ID, "pri_auth"))
        # )
        #
        # browser.implicitly_wait(10)
        # print(263, element.get_attribute('type'))
        # element.click()
    except Exception as e:
        element = WebDriverWait(browser, 30).until(
            EC.element_to_be_clickable((By.ID, "pri_auth"))
        )

        printMessage(element.get_attribute('type'), basefilename + str(getframe().f_lineno), 1)
        element.click()
        browser.save_screenshot("2-saveerror273.png")
        printMessage(str(e), basefilename + str(getframe().f_lineno), 1)

    try:
        searchElement = WebDriverWait(browser, 50).until(
            EC.presence_of_element_located((By.ID, "onMapSerachId"))
        )
        browser.find_element("id", "onMapSerachId").send_keys('635204')
        browser.find_element("id", "onMapSerachId").send_keys('')
        time.sleep(5)
    except Exception as e:
        browser.save_screenshot("2-maperror.png")
        printMessage(str(e), basefilename + str(getframe().f_lineno), 1)

    # try:
    #     localityElement = WebDriverWait(browser, 50).until(
    #         EC.presence_of_element_located((By.ID, "pd_locality"))
    #     )
    #     browser.execute_script("arguments[0].scrollIntoView(true);", localityElement)
    #     browser.find_element("id", "locality").send_keys(',')
    #     time.sleep(5)
    # except Exception as e:
    #     browser.save_screenshot("2-localityerror.png")
    #     print('ex 2-336', str(e))

    try:

        browser.implicitly_wait(20)
        listElements = browser.find_elements(By.XPATH, '//*[@id="as-results-onMapSerachId"]/ul/li')
        browser.save_screenshot("2-listElements.png")
        for list in listElements:
            if '635204' in list.text:
                list.click()
                printMessage(list.text, basefilename + str(getframe().f_lineno), 0)

                break

    except Exception as e:
        browser.save_screenshot("2-reserror.png")
        printMessage(str(e), basefilename + str(getframe().f_lineno), 1)



    # try:
    #     browser.implicitly_wait(20)
    #
    #     elementrs = WebDriverWait(browser, 30).until(
    #         EC.element_to_be_clickable((By.XPATH, '//*[@id="as-results-onMapSerachId"]/ul/li[1]'))
    #     )
    #
    #     browser.implicitly_wait(10)
    #     print(241, elementrs.get_attribute('type'))
    #     elementrs.click()
    # except Exception as e:
    #     browser.save_screenshot("2-reserror.png")
    #     print('ex 2-245', str(e))

    try:
        printMessage("second form submission enters", basefilename+str(getframe().f_lineno), 0)
        browser.implicitly_wait(20)

        elementbs = WebDriverWait(browser, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Save & Continue')]"))
        )

        # print(283, elementbs)
        browser.implicitly_wait(15)
        printMessage(elementbs.get_attribute('type'), basefilename + str(getframe().f_lineno), 0)

        elementbs.click()
        printMessage("Second form submitted", basefilename + str(getframe().f_lineno), 0)

    except Exception as e:
        elementnewb = WebDriverWait(browser, 100).until(
            EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Save & Continue')]"))
        )

        browser.implicitly_wait(10)
        elementnewb.click()
        browser.save_screenshot("2-saveerror421.png")
        printMessage(str(e), basefilename + str(getframe().f_lineno), 1)


def EditSecondSection(browser):
    try:
        printMessage("second form edit submission enters", basefilename + str(getframe().f_lineno), 0)

        browser.implicitly_wait(20)

        elementbs = WebDriverWait(browser, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Save & Continue')]"))
        )

        browser.implicitly_wait(30)
        printMessage(elementbs.get_attribute('type'), basefilename + str(getframe().f_lineno), 0)

        elementbs.click()
    except Exception as e:
        # elementnewb = WebDriverWait(browser, 30).until(
        #     EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Save & Continue')]"))
        # )
        #
        # browser.implicitly_wait(50)
        # elementnewb.click()
        browser.save_screenshot("2-saveerror444.png")
        printMessage(str(e), basefilename + str(getframe().f_lineno), 1)

    try:
        localityElement = WebDriverWait(browser, 50).until(
            EC.presence_of_element_located((By.ID, "pd_locality"))
        )
        pd_locality = localityElement.get_attribute('value')
        printMessage(pd_locality, basefilename + str(getframe().f_lineno), 0)
        time.sleep(1)
    except Exception as e:
        pd_locality = ''
        browser.save_screenshot("2-localityerror.png")
        printMessage(str(e), basefilename + str(getframe().f_lineno), 1)


    try:
        if pd_locality == '':
            browser.save_screenshot('2-alert.png')
            element = WebDriverWait(browser, 200).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="confirmDlg"]/div/div/div[2]/a[1]'))
            )
            element.click()
    except Exception as e:
        browser.save_screenshot('2-alerterror.png')
        printMessage(str(e), basefilename + str(getframe().f_lineno), 1)

