import string
import sys
import requests
import datetime

import section_five
import section_one, section_two, section_three, section_four, section_five, section_six, section_seven, section_eight
from section_one import printMessage

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
from os.path import basename

basefilename = basename(__file__)+' '
getframe = sys._getframe


def login_process(trn_number, userData):
    browser = webdriver.Chrome(service=Service('chromedriver.exe'))

    printMessage('login window opened here', basefilename + str(getframe().f_lineno), 1)

    browser.maximize_window()
    browser.get("https://reg.gst.gov.in/registration/")

    browser.implicitly_wait(5)

    # trn_number = '332200269175TRN'

    try:
        print("Start Time =", datetime.datetime.now())

        trnElement = WebDriverWait(browser, 100).until(
            EC.presence_of_element_located((By.ID, "radiotrn"))
        )
        browser.save_screenshot("trn.png")
        trnfield = browser.find_element(By.CSS_SELECTOR, '#radiotrn')
        browser.execute_script("arguments[0].click();", trnfield)

    except Exception as e:
        browser.save_screenshot("trnerror.png")
        printMessage(str(e), basefilename + str(getframe().f_lineno), 1)

    try:
        captchaElement = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, "trnno"))
        ).send_keys(trn_number)
    except Exception as e:
        printMessage(str(e), basefilename + str(getframe().f_lineno), 1)

    try:
        captchaElement = WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.ID, "captchatrn"))
        ).send_keys('')
        # browser.find_element("id", "captchatrn").send_keys('')
    except Exception as e:
        printMessage(str(e), basefilename + str(getframe().f_lineno), 1)

    try:
        captchaElement = WebDriverWait(browser, 250).until(
            EC.presence_of_element_located((By.ID, "mobile_otp"))
        ).send_keys('')
    except Exception as e:
        browser.save_screenshot("otperror.png")
        printMessage(str(e), basefilename + str(getframe().f_lineno), 1)

    try:
        table = WebDriverWait(browser, 200).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.table')))
        button = WebDriverWait(browser, 50).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.btn-primary')))
        button.click()

    except Exception as e:
        table = WebDriverWait(browser, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.table')))
        button = WebDriverWait(browser, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.btn-primary')))
        button.click()
        browser.save_screenshot('applicationserr.png')
        printMessage(str(e), basefilename + str(getframe().f_lineno), 1)

    # Checking first section compleeted or not

    try:
        browser.implicitly_wait(5)
        # element = browser.find_element(By.ID, "tnm")
        elementPara = WebDriverWait(browser, 20).until(
            EC.presence_of_element_located((By.ID, "tnm"))
        )
        browser.execute_script("arguments[0].scrollIntoView(true);", elementPara)
        browser.save_screenshot('tradefocus.png')
    except Exception as e:
        browser.save_screenshot('tradeerror.png')
        printMessage(str(e), basefilename + str(getframe().f_lineno), 1)

    browser.implicitly_wait(30)

    try:
        # browser.implicitly_wait(50)
        elementPara = WebDriverWait(browser, 100).until(
            EC.element_to_be_clickable((By.ID, "tnm"))
        )
        # slow internet

        if not elementPara.is_enabled():
            elementPara = WebDriverWait(browser, 30).until(
                EC.presence_of_element_located((By.ID, "tnm"))
            )
        trnNumberExists = elementPara.get_attribute('value')

        printMessage(trnNumberExists, basefilename + str(getframe().f_lineno), 0)
        printMessage(elementPara.is_enabled(), basefilename + str(getframe().f_lineno), 0)

        browser.save_screenshot('trnNumberExists.png')
    except Exception as e:
        trnNumberExists = ''
        browser.save_screenshot('trninerror.png')
        printMessage(str(e), basefilename + str(getframe().f_lineno), 1)

    if trnNumberExists is None or trnNumberExists =='':
        printMessage("this is new record:"+trnNumberExists, basefilename + str(getframe().f_lineno), 0)
        section_one.NewFirstSection(browser, userData)

    else:
        printMessage("this is old record:" + trnNumberExists, basefilename + str(getframe().f_lineno), 0)
        section_one.EditFirstSection(browser, userData)

    print("first form completed")
    print("first end Time =", datetime.datetime.now())
    time.sleep(5)
    # sys.exit()

    # Check whether second section completed or not

    try:
        elementSec = WebDriverWait(browser, 30).until(
            EC.presence_of_element_located((By.ID, "ffname"))
        )
        FatherExists = elementSec.get_attribute('value')
    except Exception as e:
        FatherExists = ''
        browser.save_screenshot('fathererror.png')
        printMessage(str(e), basefilename + str(getframe().f_lineno), 1)

    if FatherExists is None or FatherExists =='':
        printMessage("this is new second record:" + FatherExists, basefilename + str(getframe().f_lineno), 0)
        section_two.NewSecondSection(browser, userData)

    else:
        printMessage("this is old second record:" + FatherExists, basefilename + str(getframe().f_lineno), 0)
        section_two.EditSecondSection(browser, userData)

    time.sleep(5)
    print('Second form completed')

    if FatherExists is None or FatherExists =='':
        browser.execute_script("alert('please pick address and make sure to submit this form fully, next form only will handle by bot')")
        time.sleep(50)

    # sys.exit()
    # print('Process completed, if alert shows will handle here')

    # if no locality
    # try:
    #     browser.save_screenshot('alert.png')
    #     elementlist = WebDriverWait(browser, 200).until(
    #             EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div[3]/div/ul/li[2]'))
    #         )
    #     print(249, elementlist)
    #     print(250, elementlist.get_attribute('class'))
    #     if elementlist.get_attribute('class')!='complete':
    #         element = WebDriverWait(browser, 200).until(
    #                 EC.element_to_be_clickable((By.XPATH, '//*[@id="confirmDlg"]/div/div/div[2]/a[1]'))
    #             )
    #         element.click()
    # except Exception as e:
    #     browser.save_screenshot('alerterror.png')
    #     print("459, failed to locate alert", e)

    thirdCompleted = 0
    try:
        browser.implicitly_wait(10)
        thirdElement = WebDriverWait(browser, 80).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div[3]/div/ul/li[3]"))
        )
        printMessage(thirdElement, basefilename + str(getframe().f_lineno), 0)
        printMessage(thirdElement.get_attribute('class'), basefilename + str(getframe().f_lineno), 0)
        titleClass = thirdElement.get_attribute('class')
        if titleClass == 'active complete':
            thirdCompleted = 1

    except Exception as e:
        browser.save_screenshot("thirderror192.png")
        printMessage(str(e), basefilename + str(getframe().f_lineno), 1)

    if thirdCompleted == 1:
        section_three.EditThirdSection(browser, userData)
    else:
        section_three.NewThirdSection(browser, userData)

    # if no locality
    # try:
    #     browser.save_screenshot('alert.png')
    #     element = WebDriverWait(browser, 100).until(
    #             EC.element_to_be_clickable((By.XPATH, '//*[@id="confirmDlg"]/div/div/div[2]/a[1]'))
    #         )
    #     element.click()
    # except Exception as e:
    #     browser.save_screenshot('alerterror511.png')
    #     print("512, failed to locate alert", e)

    # try:
    #     print("second form final submission enters")
    #     browser.implicitly_wait(20)
    #
    #     elementbs = WebDriverWait(browser, 30).until(
    #         EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Save & Continue')]"))
    #     )
    #
    #     browser.implicitly_wait(30)
    #     print(492, elementbs.get_attribute('type'))
    #     elementbs.click()
    # except Exception as e:
    #     browser.save_screenshot("exiterror501.png")
    #     print('ex 502', str(e))

    print("Third form finished")
    time.sleep(10)
    # sys.exit()

    fourthCompleted = 0
    try:
        browser.implicitly_wait(10)
        fourthElement = WebDriverWait(browser, 100).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div[3]/div/ul/li[4]"))
        )
        printMessage(fourthElement, basefilename + str(getframe().f_lineno), 0)
        printMessage(fourthElement.get_attribute('class'), basefilename + str(getframe().f_lineno), 0)
        titleClass = fourthElement.get_attribute('class')
        if titleClass == 'active complete':
            fourthCompleted = 1

    except Exception as e:
        browser.save_screenshot("fourtherror243.png")
        printMessage(str(e), basefilename + str(getframe().f_lineno), 1)

    if fourthCompleted == 1:
        section_four.EditFourthSection(browser, userData)
    else:
        section_four.NewFourthSection(browser, userData)

    print("fourth form finished")

    time.sleep(10)

    fifthCompleted = 0
    try:
        browser.implicitly_wait(10)
        fifthElement = WebDriverWait(browser, 100).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div[3]/div/ul/li[5]"))
        )
        printMessage(fifthElement, basefilename + str(getframe().f_lineno), 0)
        printMessage(fifthElement.get_attribute('class'), basefilename + str(getframe().f_lineno), 0)
        titleClass = fifthElement.get_attribute('class')
        if titleClass == 'active complete':
            fifthCompleted = 1

    except Exception as e:
        browser.save_screenshot("fiftherror268.png")
        printMessage(str(e), basefilename + str(getframe().f_lineno), 1)

    print("fifth form starts")

    if fifthCompleted == 1:
        section_five.EditFifthSection(browser, userData)
    else:
        section_five.NewFifthSection(browser, userData)

    print("fifth form Submitted")

    time.sleep(10)

    sixthCompleted = 0
    try:
        browser.implicitly_wait(10)
        sixthElement = WebDriverWait(browser, 100).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div[3]/div/ul/li[6]"))
        )
        printMessage(sixthElement, basefilename + str(getframe().f_lineno), 0)
        printMessage(sixthElement.get_attribute('class'), basefilename + str(getframe().f_lineno), 0)
        titleClass = sixthElement.get_attribute('class')
        if titleClass == 'active complete':
            sixthCompleted = 1

    except Exception as e:
        browser.save_screenshot("sixtherror268.png")
        printMessage(str(e), basefilename + str(getframe().f_lineno), 1)

    print("sixth form starts")

    if sixthCompleted == 1:
        section_six.EditSixthSection(browser, userData)
    else:
        section_six.NewSixthSection(browser, userData)

    print("sixth form submitted")

    time.sleep(10)

    SeventhCompleted = 0
    try:
        browser.implicitly_wait(10)
        seventhElement = WebDriverWait(browser, 100).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div[3]/div/ul/li[7]"))
        )
        printMessage(seventhElement, basefilename + str(getframe().f_lineno), 0)
        printMessage(seventhElement.get_attribute('class'), basefilename + str(getframe().f_lineno), 0)
        titleClass = seventhElement.get_attribute('class')
        if titleClass == 'active complete':
            SeventhCompleted = 1

    except Exception as e:
        browser.save_screenshot("seventherror324.png")
        printMessage(str(e), basefilename + str(getframe().f_lineno), 1)

    print("seventh form starts")

    if SeventhCompleted == 1:
        section_seven.EditSeventhSection(browser, userData)
    else:
        section_seven.NewSeventhSection(browser, userData)

    print("seventh form submitted")

    time.sleep(10)

    EighthCompleted = 0
    try:
        browser.implicitly_wait(10)
        EighthElement = WebDriverWait(browser, 100).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div[3]/div/ul/li[8]"))
        )
        printMessage(EighthElement, basefilename + str(getframe().f_lineno), 0)
        printMessage(EighthElement.get_attribute('class'), basefilename + str(getframe().f_lineno), 0)
        titleClass = EighthElement.get_attribute('class')
        if titleClass == 'active complete':
            EighthCompleted = 1

    except Exception as e:
        browser.save_screenshot("eighterror351.png")
        printMessage(str(e), basefilename + str(getframe().f_lineno), 1)

    print("eighth form starts")

    if EighthCompleted == 1:
        section_eight.EditEighthSection(browser, userData)
    else:
        section_eight.NewEighthSection(browser, userData)

    print("eighth form submitted")

    browser.execute_script("alert('Process Completed')")

    time.sleep(2000)