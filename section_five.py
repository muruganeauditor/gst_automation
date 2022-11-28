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

def NewFifthSection(browser, userData):
    addressData = userData['businesses'][0]
    try:
        printMessage('New fifth form starts here', basefilename + str(getframe().f_lineno), 0)
        browser.save_screenshot("5-busaddress369.png")
        busElement = WebDriverWait(browser, 50).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='newRegForm']/fieldset/h4[1]/span"))
        )
    except Exception as e:
        browser.save_screenshot("5-placeerror550.png")
        printMessage(str(e), basefilename + str(getframe().f_lineno), 1)

    try:
        searchElement = WebDriverWait(browser, 50).until(
            EC.presence_of_element_located((By.ID, "onMapSerachId"))
        )
        browser.find_element("id", "onMapSerachId").send_keys('Coimbatore')
        time.sleep(5)
    except Exception as e:
        browser.save_screenshot("5-maperror560.png")
        printMessage(str(e), basefilename + str(getframe().f_lineno), 1)

    try:

        browser.implicitly_wait(20)
        listElements = WebDriverWait(browser, 100).until(
            EC.presence_of_all_elements_located((By.XPATH, '//*[@id="as-results-onMapSerachId"]/ul/li'))
        )
        # print(listElements.get_attribute('innerHTML'))
        # listElements = browser.find_elements(By.XPATH, '//*[@id="as-results-onMapSerachId"]/ul/li')
        browser.save_screenshot("listElements.png")
        for list in listElements:
            if 'Coimbatore' in list.text:
                # print(list.get_attribute('innerHTML'))
                printMessage(list.text, basefilename + str(getframe().f_lineno), 0)
                # print(298, list.text)
                list.click()
                break
        browser.implicitly_wait(10)

        # elementbs = WebDriverWait(browser, 20).until(
        #     EC.element_to_be_clickable((By.ID, "confirm-mapquery-btn3"))
        # ).click()


        # element = browser.find_element(By.ID, "confirm-mapquery-btn3")
        # browser.execute_script("arguments[0].scrollIntoView(true);", element)

        browser.execute_script("$('#confirm-mapquery-btn3').trigger('click')")

    except Exception as e:
        browser.save_screenshot("5-reserror.png")
        printMessage(str(e), basefilename + str(getframe().f_lineno), 1)

    # try:
    #     printMessage("looking for jurisdiction", basefilename + str(getframe().f_lineno), 0)
    #     browser.implicitly_wait(20)
    #
    #     formElement = WebDriverWait(browser, 400).until(
    #         EC.presence_of_element_located((By.XPATH, "//*[@id='stj']/option[2]"))
    #     )
    #     formElement.click()
    #     printMessage(formElement.text, basefilename + str(getframe().f_lineno), 0)
    # except Exception as e:
    #     browser.save_screenshot("5-reserror.png")
    #     printMessage(str(e), basefilename + str(getframe().f_lineno), 1)

    printMessage("autocompletion finished", basefilename + str(getframe().f_lineno), 0)

    browser.execute_script(
        "alert('please pick address and make sure to fill address details, from jurisdiction will handle by bot')")
    time.sleep(30)

    try:
        browser.implicitly_wait(20)

        formElement = WebDriverWait(browser, 400).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='comcd']/option[2]"))
        )
        formElement.click()
    except Exception as e:
        printMessage(str(e), basefilename + str(getframe().f_lineno), 1)

    # try:
    #     stat = browser.find_element("id", "comcd")
    #     statt = Select(stat)
    # except Exception as e:
    #     printMessage(str(e), basefilename + str(getframe().f_lineno), 1)
    #     stat = browser.find_element("id", "comcd")
    #     statt = Select(stat)
    #
    # printMessage('Commissionerate Options loading', basefilename + str(getframe().f_lineno), 0)
    # # iterate over dropdown options
    # for opt in statt.options:
    #
    #     if 'COIMBATORE' in opt.text:
    #         sel = Select(browser.find_element("id", 'comcd'))
    #
    #         sel.select_by_visible_text(opt.text)
    #         printMessage(opt.text, basefilename + str(getframe().f_lineno), 0)
    #
    #         time.sleep(0.8)
    #         break

    browser.implicitly_wait(15)

    try:
        browser.implicitly_wait(5)

        formElement = WebDriverWait(browser, 400).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='divcd']/option[2]"))
        )
        formElement.click()
    except Exception as e:
        printMessage(str(e), basefilename + str(getframe().f_lineno), 1)

    # try:
    #     citya = browser.find_element("id", "divcd")
    #     citys = Select(citya)
    # except Exception as e:
    #     printMessage(str(e), basefilename + str(getframe().f_lineno), 1)
    #     citya = browser.find_element("id", "divcd")
    #     citys = Select(citya)
    #
    # browser.implicitly_wait(15)
    # print('division Options loading')
    #
    # # iterate over dropdown options
    # for opt in citys.options:
    #
    #     sel = Select(browser.find_element("id", 'divcd'))
    #
    #     sel.select_by_visible_text(opt.text)
    #     printMessage(opt.text, basefilename + str(getframe().f_lineno), 0)
    #     time.sleep(0.8)
    #     break
    #
    # browser.implicitly_wait(15)
    #
    # try:
    #     range = browser.find_element("id", "rgcd")
    #     ranges = Select(range)
    # except Exception as e:
    #     printMessage(str(e), basefilename + str(getframe().f_lineno), 1)
    #     range = browser.find_element("id", "rgcd")
    #     ranges = Select(range)
    #
    # browser.implicitly_wait(15)
    # print('range Options loading')
    #
    # # iterate over dropdown options
    # for opt in ranges.options:
    #
    #     sel = Select(browser.find_element("id", 'rgcd'))
    #
    #     sel.select_by_visible_text(opt.text)
    #     printMessage(opt.text, basefilename + str(getframe().f_lineno), 0)
    #     time.sleep(0.8)
    #     break

    try:
        browser.implicitly_wait(5)

        formElement = WebDriverWait(browser, 400).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='rgcd']/option[2]"))
        )
        formElement.click()
    except Exception as e:
        printMessage(str(e), basefilename + str(getframe().f_lineno), 1)


    # file upload
    try:
        sel = Select(browser.find_element("id", 'bp_buss_poss'))
        sel.select_by_value(addressData['nature_profession'])

    except Exception as e:
        printMessage(str(e), basefilename + str(getframe().f_lineno), 1)

    browser.implicitly_wait(15)
    print(addressData)

    for proofDb in addressData['proofs']:
        print(proofDb)
        try:
            sel = Select(browser.find_element("id", 'bp_up_type'))
            browser.implicitly_wait(10)
            sel.select_by_value(proofDb['business_place_proof'])

        except Exception as e:
            printMessage(str(e), basefilename + str(getframe().f_lineno), 1)

        try:
            if proofDb['id'] == 6:
                fileElement = WebDriverWait(browser, 200).until(
                    EC.presence_of_element_located((By.ID, "bp_upload"))
                ).send_keys('C:\\Users\\Murugan\\Desktop\\WhatsApp.jpeg')
            else:
                fileElement = WebDriverWait(browser, 200).until(
                    EC.presence_of_element_located((By.ID, "bp_upload"))
                ).send_keys('C:\\Users\\Murugan\\Desktop\\download.jpg')
            printMessage('upload', basefilename + str(getframe().f_lineno), 1)
        except Exception as e:
            browser.save_screenshot("5-file.png")
            printMessage(str(e), basefilename + str(getframe().f_lineno), 1)

    busTypeDb = addressData['naturebusact'].split(',')

    for bustype in busTypeDb:
        try:
            # business_type = 'Retail Business'
            # forname = browser.find_element(By.XPATH, "//li//label[contains( text( ), '" + business_type + "')]").get_attribute(
            #     'for')
            print(bustype,basefilename + str(getframe().f_lineno), 0)
            activity = browser.find_element(By.CSS_SELECTOR, '#bp_ck_'+bustype.replace(' ',''))
            browser.execute_script("arguments[0].click();", activity)
        except Exception as e:
            browser.save_screenshot("5-business.png")
            printMessage(str(e), basefilename + str(getframe().f_lineno), 1)

    try:
        printMessage("fifth form submission enters", basefilename + str(getframe().f_lineno), 0)
        browser.implicitly_wait(30)

        formElement = WebDriverWait(browser, 100).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Save & Continue')]"))
        )

        elementbs = WebDriverWait(browser, 100).until(
            EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Save & Continue')]"))
        )

        browser.implicitly_wait(20)
        printMessage(elementbs.get_attribute('type'), basefilename + str(getframe().f_lineno), 0)
        browser.execute_script("arguments[0].click();", elementbs)
        printMessage('save & continue button submitted', basefilename + str(getframe().f_lineno), 0)
    except Exception as e:
        browser.save_screenshot("5-fourerror229.png")
        printMessage(str(e), basefilename + str(getframe().f_lineno), 1)

def EditFifthSection(browser, userData):
    try:
        printMessage("fifth edit form submission enters", basefilename + str(getframe().f_lineno), 0)
        browser.implicitly_wait(30)

        formElement = WebDriverWait(browser, 100).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Save & Continue')]"))
        )

        elementbs = WebDriverWait(browser, 100).until(
            EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Save & Continue')]"))
        )

        browser.implicitly_wait(20)
        printMessage(elementbs.get_attribute('type'), basefilename + str(getframe().f_lineno), 0)
        browser.execute_script("arguments[0].click();", elementbs)
        printMessage('save & continue button submitted', basefilename + str(getframe().f_lineno), 0)
    except Exception as e:
        browser.save_screenshot("5-fourerror229.png")
        printMessage(str(e), basefilename + str(getframe().f_lineno), 1)