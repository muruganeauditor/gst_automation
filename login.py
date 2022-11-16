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

browser = webdriver.Chrome(service=Service('chromedriver.exe'))

browser.maximize_window()
browser.get("https://reg.gst.gov.in/registration/")

browser.implicitly_wait(5)

trn_number = '332200266410TRN'

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
    print('radio 38', str(e))

try:
    captchaElement = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.ID, "trnno"))
    ).send_keys(trn_number)
except Exception as e:
    print('ex 45', str(e))

try:
    captchaElement = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.ID, "captchatrn"))
    ).send_keys('')
    # browser.find_element("id", "captchatrn").send_keys('')
except Exception as e:
    print('ex 53', str(e))

try:
    captchaElement = WebDriverWait(browser, 200).until(
        EC.presence_of_element_located((By.ID, "mobile_otp"))
    ).send_keys('')
except Exception as e:
    browser.save_screenshot("otperror.png")
    print('ex 61', str(e))

try:
    table = WebDriverWait(browser, 200).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.table')))
    button = WebDriverWait(browser, 50).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.btn-primary')))
    button.click()

except Exception as e:
    table = WebDriverWait(browser, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.table')))
    button = WebDriverWait(browser, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.btn-primary')))
    button.click()
    browser.save_screenshot('applicationserr.png')
    print("73 failed to locate edit button", e)

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
    print('ex 85', str(e))

try:
    elementPara = WebDriverWait(browser, 20).until(
        EC.presence_of_element_located((By.ID, "tnm"))
    )
    trnNumberExists = elementPara.get_attribute('value')
except Exception as e:
    trnNumberExists = ''
    browser.save_screenshot('trninerror.png')
    print('ex 94', str(e))

def NewFirstSection():
    try:
        print("New form started")
        elementPara = WebDriverWait(browser, 20).until(
            EC.presence_of_element_located((By.ID, "tnm"))
        ).send_keys('Test trades')
        # browser.find_element("id", "tnm").send_keys('Test trades')
    except Exception as e:
        browser.save_screenshot('tradeinerror.png')
        print('ex 94', str(e))

    try:
        sel = Select(browser.find_element("id", 'bd_ConstBuss'))
        browser.implicitly_wait(10)
        sel.select_by_value("PRO")

    except Exception as e:
        print("102", e)

    try:
        sel = Select(browser.find_element("id", 'bd_rsl'))
        browser.implicitly_wait(10)
        sel.select_by_value("VOLN")

    except Exception as e:
        print("110", e)

    try:
        browser.implicitly_wait(20)
        element = browser.find_element(By.ID, "bd_cmbz")
        browser.execute_script("arguments[0].scrollIntoView(true);", element)
        print("Date field located")
    except Exception as e:
        browser.save_screenshot('bderror.png')
        print('ex 118', str(e))

    try:
        captchaElement = WebDriverWait(browser, 250).until(
            EC.presence_of_element_located((By.ID, "bd_cmbz"))
        ).send_keys('12/11/2021')
        print("date filed filled")
    except Exception as e:
        browser.save_screenshot("date.png")
        print('ex 126', str(e))

    try:
        fileElement = WebDriverWait(browser, 200).until(
            EC.presence_of_element_located((By.ID, "tr_upload"))
        ).send_keys('C:\\Users\\Murugan\\Desktop\\WhatsApp.jpeg')
    except Exception as e:
        browser.save_screenshot("file.png")
        print('ex 135', str(e))

    # try:
    #     print("entering into save and continue")
    #     browser.implicitly_wait(20)
    #
    #     element = WebDriverWait(browser, 30).until(
    #         EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Save & Continue')]"))
    #     )
    #
    #     print(145, element)
    #     browser.implicitly_wait(30)
    #     print(147, element.get_attribute('type'))
    #     print("save and continue works")
    #     element.click()
    # except Exception as e:
    #     elementnew = WebDriverWait(browser, 30).until(
    #         EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Save & Continue')]"))
    #     )
    #
    #     elementnew.click()
    #     browser.save_screenshot("saveerror156.png")
    #     print('ex 157', str(e))

def NewSecondSection():
    try:
        print("enters into second new form")
        browser.implicitly_wait(10)

        elementPara = WebDriverWait(browser, 50).until(
            EC.presence_of_element_located((By.ID, "ffname"))
        )
        browser.execute_script("arguments[0].scrollIntoView(true);", elementPara)
        browser.save_screenshot('fatherfocus.png')
        fnameElement = WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.ID, "ffname"))
        ).send_keys('Palani')
    except Exception as e:
        browser.save_screenshot('fathererror.png')
        print('ex 172', str(e))

    try:
        browser.implicitly_wait(10)
        fnameElement = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, "pd_flname"))
        ).send_keys('Vediyappan')
    except Exception as e:
        browser.save_screenshot('fatherlerror.png')
        print('ex 181', str(e))

    try:
        dobElement = WebDriverWait(browser, 200).until(
            EC.presence_of_element_located((By.ID, "dob"))
        ).send_keys('12/05/1990')
        elementdob = WebDriverWait(browser, 20).until(
            EC.presence_of_element_located((By.ID, "dob"))
        )
        dobExists = elementdob.get_attribute('value')
        if dobExists=='':
            dobElement = WebDriverWait(browser, 200).until(
                EC.presence_of_element_located((By.ID, "dob"))
            ).send_keys('12/05/1990')
    except Exception as e:
        browser.save_screenshot("doberror.png")
        print('ex 189', str(e))

    try:
        mobileElement = WebDriverWait(browser, 50).until(
            EC.presence_of_element_located((By.ID, "mbno"))
        ).send_keys('9585393730')
    except Exception as e:
        browser.save_screenshot("mobileerror.png")
        print('ex 197', str(e))

    try:
        mobileElement = WebDriverWait(browser, 50).until(
            EC.presence_of_element_located((By.ID, "pd_email"))
        ).send_keys('muruganaccetcse@gmail.com')
    except Exception as e:
        browser.save_screenshot("emailerror.png")
        print('ex 205', str(e))

    try:
        browser.implicitly_wait(5)
        gender = 'Male'

        genderfield = browser.find_element(By.CSS_SELECTOR, '#radiomale')
        print(gender, genderfield)
        browser.execute_script("arguments[0].click();", genderfield)
    except Exception as e:
        print('gender 215', str(e))

    try:
        desElement = WebDriverWait(browser, 50).until(
            EC.presence_of_element_located((By.ID, "dg"))
        ).send_keys('Proprietor')
    except Exception as e:
        browser.save_screenshot("proerror.png")
        print('ex 223', str(e))

    try:
        searchElement = WebDriverWait(browser, 50).until(
            EC.presence_of_element_located((By.ID, "onMapSerachId"))
        ).send_keys('635204')
        browser.implicitly_wait(5)
    except Exception as e:
        browser.save_screenshot("maperror.png")
        print('ex 231', str(e))

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
    #     browser.save_screenshot("reserror.png")
    #     print('ex 245', str(e))

    try:
        fileElement = WebDriverWait(browser, 200).until(
            EC.presence_of_element_located((By.ID, "pd_upload"))
        ).send_keys('C:\\Users\\Murugan\\Desktop\\download.jpg')
    except Exception as e:
        browser.save_screenshot("profile.png")
        print('ex 253', str(e))

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

        print(271, element.get_attribute('type'))
        element.click()
        browser.save_screenshot("saveerror273.png")
        print('ex 274', str(e))


if trnNumberExists is None or trnNumberExists =='':
    print("this is new record", trnNumberExists)
    NewFirstSection()

    try:
        print("entering into save and continue")
        browser.implicitly_wait(20)

        element = WebDriverWait(browser, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Save & Continue')]"))
        )

        # print(145, element)
        browser.implicitly_wait(30)
        print(147, element.get_attribute('type'))
        print("save and continue works")
        element.click()

    except Exception as e:
        elementnew = WebDriverWait(browser, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Save & Continue')]"))
        )

        elementnew.click()
        browser.save_screenshot("saveerror156.png")
        print('ex 157', str(e))
else:
    print("this is old record", trnNumberExists)
    try:
        print("entering into save and continue")
        browser.implicitly_wait(20)

        element = WebDriverWait(browser, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Save & Continue')]"))
        )

        # print(145, element)
        browser.implicitly_wait(30)
        print(147, element.get_attribute('type'))
        print("save and continue works")
        element.click()
    except Exception as e:
        elementnew = WebDriverWait(browser, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Save & Continue')]"))
        )

        elementnew.click()
        browser.save_screenshot("saveerror156.png")
        print('ex 157', str(e))

print("first form completed")
print("first end Time =", datetime.datetime.now())

try:
    elementSec = WebDriverWait(browser, 20).until(
        EC.presence_of_element_located((By.ID, "ffname"))
    )
    FatherExists = elementSec.get_attribute('value')
except Exception as e:
    FatherExists = ''
    browser.save_screenshot('fathererror.png')
    print('ex 94', str(e))

if FatherExists is None or FatherExists =='':
    print("this is new second-record", FatherExists)
    NewSecondSection()
    try:
        print("second form submission enters")
        browser.implicitly_wait(20)

        elementbs = WebDriverWait(browser, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Save & Continue')]"))
        )

        # print(283, elementbs)
        browser.implicitly_wait(15)
        print(285, elementbs.get_attribute('type'))
        elementbs.click()
        print("Second form submitted")
    except Exception as e:
        elementnewb = WebDriverWait(browser, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Save & Continue')]"))
        )

        browser.implicitly_wait(20)
        elementnewb.click()
        browser.save_screenshot("saveerror294.png")
        print('ex 295', str(e))
else:
    print("this is old second-record", FatherExists)
    try:
        print("second form submission enters")
        browser.implicitly_wait(20)

        elementbs = WebDriverWait(browser, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Save & Continue')]"))
        )

        print(283, elementbs)
        browser.implicitly_wait(30)
        print(285, elementbs.get_attribute('type'))
        elementbs.click()
    except Exception as e:
        elementnewb = WebDriverWait(browser, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Save & Continue')]"))
        )

        browser.implicitly_wait(50)
        elementnewb.click()
        browser.save_screenshot("saveerror294.png")
        print('ex 295', str(e))

browser.execute_script("alert('process completed')")

print('Process completed')
time.sleep(500)
