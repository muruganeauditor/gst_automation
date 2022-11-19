import string
import sys
import requests
import datetime
import login

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


browser = webdriver.Chrome(service=Service('C:\\Users\\Liva\\Desktop\\gst_automation\\chromedriver.exe'))

browser.maximize_window()
browser.get("https://reg.gst.gov.in/registration/")

browser.implicitly_wait(5)

try:
    print("inside tax")
    sel = Select(browser.find_element("id", 'applnType'))

    sel.select_by_value("APLRG")

except Exception as e:
    print("94",e)

try:
    browser.implicitly_wait(5)
    stat = browser.find_element("id", "applnState")
    statt = Select(stat)
except Exception as e:
    print('state 390', str(e))
    stat = browser.find_element("id", "applnState")
    statt = Select(stat)

print('state Options loading')
print('state', 'Tamil Nadu')
# iterate over dropdown options
for opt in statt.options:
    # print(opt.text)
    if 'Tamil Nadu' in opt.text:
        sel = Select(browser.find_element("id", 'applnState'))

        sel.select_by_visible_text(opt.text)
        # print(opt.text)
        time.sleep(0.8)
        break

browser.implicitly_wait(15)

try:
    citya = browser.find_element("id", "applnDistr")
    citys = Select(citya)
except Exception as e:
    print('citys 293', str(e))
    citya = browser.find_element("id", "applnDistr")
    citys = Select(citya)

browser.implicitly_wait(15)
print('city Options loading')
# iterate over dropdown options
for opt in citys.options:
    # print(opt.text)
    if 'Krishnagiri' in opt.text:
        sel = Select(browser.find_element("id", 'applnDistr'))

        sel.select_by_visible_text(opt.text)
        print(opt.text)
        time.sleep(0.8)
        break

browser.implicitly_wait(15)

try:
    browser.find_element("id", "bnm").send_keys('Palani Murugan')
except Exception as e:
    print('state 61', str(e))


try:
    browser.find_element("id", "pan_card").send_keys('CLNPM9204L')
except Exception as e:
    print('state 61', str(e))


try:
    browser.implicitly_wait(2)
    browser.find_element("id", "email").send_keys('murugan@eauditoroffice.com')
except Exception as e:
    print('ex 74', str(e))

try:
    mobileElement = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.ID, "mobile"))
    )
    browser.find_element("id", "mobile").send_keys('9585393730')
except Exception as e:
    print('ex 82', str(e))


try:
    mobileElement = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.ID, "mobile"))
    )
    browser.find_element("id", "captcha").send_keys('')
except Exception as e:
    print('ex 82', str(e))

print(93, 'sleep')
time.sleep(50)
browser.implicitly_wait(50)
print(95, 'going to look alert')
try:
    elementPara = WebDriverWait(browser, 1000).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/div/div[2]/div/div[2]/div/div[1]/div/p"))
    )
    # print(102, elementPara)
    a = browser.find_element(By.CLASS_NAME, "alert-success")
    print(104, a.text)
    browser.save_screenshot('alert.png')
   
except Exception as e:
    browser.save_screenshot('after.png')
    print('ex 103', str(e))

print(107, 'going to look trn no')
trnno_new = ''
try:
    element = WebDriverWait(browser, 300).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/div/div[2]/div/div[2]/div/div[1]/div/p/span[2]"))
        )
    trnno_val = element.text
    print('100', element, element.text)
    trnno_new = browser.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div[2]/div/div[2]/div/div[1]/div/p/span[2]").text
    print(trnno_new)
except Exception as e:
    print("120 failed to locate alert", e)
    sys.exit(e)

try:
    browser.save_screenshot('trnlook.png')
    element = WebDriverWait(browser, 100).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/div/a"))
        )
    browser.execute_script("arguments[0].innerHTML = arguments[1];", element, "<h2>This is from bot,<br> please wait this window will close and <br> new window will be opened!</h2>")
except Exception as e:
    browser.save_screenshot('trnerror.png')
    print("130, failed to locate button", e)
#
# elm = driver.find_element_by_xpath(".//*[@id='content']")
# browser.execute_script("arguments[0].innerHTML = arguments[1];", elm, img);
#
# browser.execute_script("$('form').append('<h1>This is from bot, please wait this window will close and new window will be opened!</h1>')")
# content = '<br><br><h1 style="color:red">This is from bot, please wait this window will close and new window will be opened!</h1><br><br>'
# browser.execute_script(f'$("form").append({content})')
# time.sleep(200)
#
# print("login process will begin here")
# try:
#     browser.execute_script("alert('Registration process completed, login will begin soon, please wait')")
#
# except Exception as e:
#     browser.save_screenshot('ralerterror.png')
#     print("130, failed to locate button", e)

# try:
#     alert = browser.switch_to_alert()
#     print(alert.text)
#     alert.accept()
# except:
#     print("no alert to accept")


try:
    if trnno_new != '':
        browser.close()
        browser.quit()
        login.login_process(trnno_new)
except Exception as e:
    print("failed to login")
# login button
# try:
#     browser.save_screenshot('trnlook.png')
#     element = WebDriverWait(browser, 30).until(
#             EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/div/a"))
#         )
#     element.click()
# except Exception as e:
#     browser.save_screenshot('trnerror.png')
#     print("130, failed to locate button", e)

# try:
#     browser.implicitly_wait(5)
#     browser.find_element("id", "trnno").send_keys(trnno_val)
# except Exception as e:
#     print('ex 137', str(e))
#
# try:
#     captchaElement = WebDriverWait(browser, 5).until(
#         EC.presence_of_element_located((By.ID, "captchatrn"))
#     )
#     browser.find_element("id", "captchatrn").send_keys('')
# except Exception as e:
#     print('ex 145', str(e))
#
# try:
#     browser.save_screenshot('otpelement.png')
#     mobileElement = WebDriverWait(browser, 250).until(
#         EC.presence_of_element_located((By.ID, "mobile_otp"))
#     )
#
#     mobilefield = browser.find_element(By.CSS_SELECTOR, '#mobile_otp')
#     browser.execute_script("arguments[0].focus();", mobilefield)
# except Exception as e:
#     browser.save_screenshot('otperror.png')
#     print('ex 154', str(e))
#
# time.sleep(100)
# browser.implicitly_wait(200)
#
# try:
#     browser.save_screenshot('applications.png')
#     element = WebDriverWait(browser, 200).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.btn-primary')))
#     browser.execute_script("arguments[0].onclick();", element)
#
#     # element = WebDriverWait(browser, 4000).until(
#     #         EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[1]/div/div[3]/div[2]/div/div/table/tbody/tr/td[6]/button"))
#     #     )
#     # element.click()
#     # print(elem.text)
# except Exception as e:
#     email = WebDriverWait(browser, 200).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.table')))
#
#     element = WebDriverWait(browser, 100).until(
#             EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[1]/div/div[3]/div[2]/div/div/table/tbody/tr/td[6]/button"))
#         )
#     # EC.presence_of_element_located((By.CSS_SELECTOR, ".ng-binding.ng-scope")))
#     # wait.until(EC.presenceOfElementLocated(By.id("table")));
#     browser.save_screenshot('applicationserr.png')
#     print("166 failed to locate edit button", e)
#
#
# try:
#     browser.implicitly_wait(5)
#     browser.save_screenshot('trade.png')
#     browser.find_element("id", "tdNam").send_keys("Test trade")
# except Exception as e:
#     browser.save_screenshot('tradeerror.png')
#     print('ex 175', str(e))

# browser.execute_script("alert('Registration process completed')")

# print('Process completed')
# time.sleep(500)
