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


browser = webdriver.Chrome(service=Service('C:\\Users\\Liva\\Desktop\\gst_automation\\chromedriver.exe'))

browser.maximize_window()
browser.get("https://reg.gst.gov.in/registration/")

browser.implicitly_wait(5)

try:
    print("inside tax")
    sel = Select(browser.find_element("id", 'applnType'))

    sel.select_by_value("APLTD")

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
    browser.find_element("id", "bnm").send_keys('Palani Murugan')
except Exception as e:
    print('state 61', str(e))


try:
    browser.find_element("id", "pan_card").send_keys('CLNPM9204L')
except Exception as e:
    print('state 61', str(e))


try:
    browser.implicitly_wait(2)
    browser.find_element("id", "email").send_keys('muruganaccetcse@gmail.com')
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
time.sleep(100)
browser.implicitly_wait(200)
print(95, 'going to look alert')
try:
    elementPara = WebDriverWait(browser, 400).until(
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
try:
    element = WebDriverWait(browser, 6000).until(
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
    element = WebDriverWait(browser, 30).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/div/a"))
        )
    element.click()
except Exception as e:
    browser.save_screenshot('trnerror.png')
    print("130, failed to locate button", e)


try:
    browser.implicitly_wait(5)
    browser.find_element("id", "trnno").send_keys(trnno_val)
except Exception as e:
    print('ex 137', str(e))

try:
    captchaElement = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.ID, "captchatrn"))
    )
    browser.find_element("id", "captchatrn").send_keys('')
except Exception as e:
    print('ex 145', str(e))

try:
    browser.save_screenshot('otpelement.png')
    mobileElement = WebDriverWait(browser, 250).until(
        EC.presence_of_element_located((By.ID, "mobile_otp"))
    )
    
    mobilefield = browser.find_element(By.CSS_SELECTOR, '#mobile_otp')
    browser.execute_script("arguments[0].focus();", mobilefield)
except Exception as e:
    browser.save_screenshot('otperror.png')
    print('ex 154', str(e))

time.sleep(100)
browser.implicitly_wait(200)

try:
    browser.save_screenshot('applications.png')
    element = WebDriverWait(browser, 4000).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[1]/div/div[3]/div[2]/div/div/table/tbody/tr/td[6]/button"))
        )
    element.click()
    print(elem.text)
except Exception as e:
    email = WebDriverWait(browser, 200).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.table')))

    element = WebDriverWait(browser, 100).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[1]/div/div[3]/div[2]/div/div/table/tbody/tr/td[6]/button"))
        )
    # EC.presence_of_element_located((By.CSS_SELECTOR, ".ng-binding.ng-scope")))
    # wait.until(EC.presenceOfElementLocated(By.id("table")));
    browser.save_screenshot('applicationserr.png')
    print("166 failed to locate edit button", e)


try:
    browser.implicitly_wait(5)
    browser.save_screenshot('trade.png')
    browser.find_element("id", "tdNam").send_keys("Test trade")
except Exception as e:
    browser.save_screenshot('tradeerror.png')
    print('ex 175', str(e))


# try:
#     print("inside tax")
#     sel = Select(browser.find_element("id", 'applnState'))

#     sel.select_by_value("33")
#     gstfield = browser.find_element(By.CSS_SELECTOR, '#applnState')
#     browser.execute_script("arguments[0].onchange();", gstfield)

# except Exception as e:
#     print("94",e)

time.sleep(100)
sys.exit()

# browser.find_element("id", "ctl00_ContentPlaceHolder1_txtadharno").send_keys(aadhaar.replace(' ', ''))
# browser.find_element("id", "ctl00_ContentPlaceHolder1_txtownername").send_keys(name)

# browser.implicitly_wait(3)

# aadharNewButton = WebDriverWait(browser, 5).until(
#         EC.element_to_be_clickable((By.ID, "ctl00_ContentPlaceHolder1_btnValidateAadhaar")))

# aadharNewButton.click()

# print("button clicks")

# try:
#     element = WebDriverWait(browser, 10).until(
#             EC.presence_of_element_located((By.ID, "ctl00_ContentPlaceHolder1_txtOtp1"))
#         )
#     element.send_keys("")

# except Exception as e:
#     print("62", e)

# try:
#     element = WebDriverWait(browser, 4000).until(
#             EC.presence_of_element_located((By.ID, "ctl00_ContentPlaceHolder1_ddlTypeofOrg"))
#         )
# except Exception as e:
#     print("failed to locate dropdown")
#     sys.exit(e)

# print(72, element.get_attribute("name"))

# # browser.execute_script("window.scrollTo(0, 200)")

# # # print(browser.page_source)

# print('type', organization_type_id)

# try:
#     l = browser.find_element("id", "ctl00_ContentPlaceHolder1_ddlTypeofOrg")
#     d = Select(element)
# except Exception as e:
#     print("84",e)

# print('Options are loaded: ')
# # iterate over dropdown options
# try:
#     sel = Select(browser.find_element("id", 'ctl00_ContentPlaceHolder1_ddlTypeofOrg'))

#     sel.select_by_value(organization_type_id)

# except Exception as e:
#     print("94",e)

# time.sleep(6)
# browser.find_element("id", "ctl00_ContentPlaceHolder1_txtPan").send_keys(pan)
# panelement = WebDriverWait(browser, 1).until(
#             EC.presence_of_element_located((By.ID, "ctl00_ContentPlaceHolder1_txtPan"))
#         )

# if panelement.get_attribute("value") == '':
#     browser.find_element("id", "ctl00_ContentPlaceHolder1_txtPan").send_keys(pan)
#     print("not value")

# PanButton = WebDriverWait(browser, 20).until(
# EC.element_to_be_clickable((By.ID, "ctl00_ContentPlaceHolder1_btnValidatePan")))
# PanButton.click()

# try:
#     PanNewButton = WebDriverWait(browser, 20).until(
#         EC.element_to_be_clickable((By.ID, "ctl00_ContentPlaceHolder1_btnGetPanData")))
#     PanNewButton.click()

# except Exception as e:
#     panError = browser.find_element("id", "ctl00_ContentPlaceHolder1_lblPanError").text
#     if "PAN is not valid" in panError:
#         browser.execute_script("alert('Invalid PAN Number')")
#         sys.exit()
#         browser.close()
#         browser.quit()

#     print('panbutton 123', str(e))


# try:
#     browser.implicitly_wait(5)

#     gst_for = browser.find_element(By.XPATH, "//*[@id='ctl00_ContentPlaceHolder1_rblWhetherGstn']//td//label[contains( text( ), '" + have_gstn + "')]").get_attribute(
#         'for')
#     print('gst', have_gstn)
#     gstfield = browser.find_element(By.CSS_SELECTOR, '#' + gst_for)
#     print('gstid', gstfield)
#     browser.execute_script("arguments[0].click();", gstfield)
# except Exception as e:
#     print('gst 136', str(e))

# try:
#     mobileElement = WebDriverWait(browser, 5).until(
#         EC.presence_of_element_located((By.ID, "ctl00_ContentPlaceHolder1_txtmobile"))
#     )
#     browser.find_element("id", "ctl00_ContentPlaceHolder1_txtmobile").send_keys(mobile)
# except Exception as e:
#     print('ex 144', str(e))



# print('category', social_category)
# try:
#     forname = browser.find_element(By.XPATH, "//td//label[contains( text( ), '" + social_category + "')]").get_attribute('for')
#     caste = browser.find_element(By.CSS_SELECTOR, '#' + forname)
#     browser.execute_script("arguments[0].click();", caste)
# except Exception as e:
#     print('category 158', str(e))

# try:
#     browser.implicitly_wait(5)

#     gen_for = browser.find_element(By.XPATH, "//td//label[contains( text( ), '" + gender + "')]").get_attribute(
#         'for')
#     print(gender, gen_for)
#     genderfield = browser.find_element(By.CSS_SELECTOR, '#' + gen_for)
#     print(gender, genderfield)
#     browser.execute_script("arguments[0].click();", genderfield)
# except Exception as e:
#     print('gender 170', str(e))

# try:
#     browser.implicitly_wait(5)

#     abled_for = browser.find_element(By.XPATH, "//td//label[contains( text( ), '" + specially_abled + "')]").get_attribute(
#         'for')
#     print('abled', abled_for)
#     abledfield = browser.find_element(By.CSS_SELECTOR, '#' + abled_for)
#     print('abledid', abledfield)
#     browser.execute_script("arguments[0].click();", abledfield)
# except Exception as e:
#     print('gst 182', str(e))

# try:
#     browser.find_element("id", "ctl00_ContentPlaceHolder1_txtenterprisename").send_keys(enterprise_name)
# except Exception as e:
#     print('ex 187', str(e))

# try:
#     unitElement = WebDriverWait(browser, 5).until(
#         EC.presence_of_element_located((By.ID, "ctl00_ContentPlaceHolder1_txtUnitName"))
#     ).send_keys(enterprise_name)
# except Exception as e:
#     print('ex 194', str(e))

# try:
#     unitElements = WebDriverWait(browser, 1).until(
#         EC.element_to_be_clickable((By.ID, "ctl00_ContentPlaceHolder1_btnAddUnit"))
#     ).click()
# except Exception as e:
#     print('ex 201', str(e))

# try:
#     browser.implicitly_wait(10)
#     element = browser.find_element(By.ID, "ctl00_ContentPlaceHolder1_ddlUnitName")
#     browser.execute_script("arguments[0].scrollIntoView(true);", element)
#     unitElementsnew = WebDriverWait(browser, 10).until(
#         EC.presence_of_element_located((By.ID, "ctl00_ContentPlaceHolder1_ddlUnitName") )
#     )
#     time.sleep(5)
#     sel = Select(browser.find_element("id", 'ctl00_ContentPlaceHolder1_ddlUnitName'))

#     sel.select_by_value('1')
# except Exception as e:
#     print('ex 215', str(e))

# try:
#     elementFlat = browser.find_element(By.ID, "ctl00_ContentPlaceHolder1_txtPFlat")

#     actions = ActionChains(browser)
#     actions.move_to_element(elementFlat).perform()
#     print("Action ok")
# except Exception as e:
#     print('FlatNo 224', str(e))

# try:
#     flatElement = WebDriverWait(browser, 10).until(
#             EC.presence_of_element_located((By.ID, "ctl00_ContentPlaceHolder1_txtPFlat"))
#         ).send_keys(flat_no)

#     browser.find_element("id", "ctl00_ContentPlaceHolder1_txtPFlat").send_keys(flat_no)
#     print("flatp ok")
# except Exception as e:
#     print('flatp 234', str(e))

# try:
#     browser.find_element("id", "ctl00_ContentPlaceHolder1_txtPBuilding").send_keys(name_of_building)
# except Exception as e:
#     print('name_of_building 239', str(e))

# try:
#     browser.find_element("id", "ctl00_ContentPlaceHolder1_txtPVillageTown").send_keys(village_town)
# except Exception as e:
#     print('village_town 244', str(e))

# try:
#     browser.find_element("id", "ctl00_ContentPlaceHolder1_txtPBlock").send_keys(block)
# except Exception as e:
#     print('block 249', str(e))

# try:
#     browser.find_element("id", "ctl00_ContentPlaceHolder1_txtPRoadStreetLane").send_keys(road_street)
# except Exception as e:
#     print('road_street 254', str(e))

# try:
#     browser.find_element("id", "ctl00_ContentPlaceHolder1_txtPCity").send_keys(city)
# except Exception as e:
#     print('city 259', str(e))

# try:
#     browser.find_element("id", "ctl00_ContentPlaceHolder1_txtPpin").send_keys(pincode)
# except Exception as e:
#     print('pincode 264', str(e))

# try:
#     stat = browser.find_element("id", "ctl00_ContentPlaceHolder1_ddlPState")
#     statt = Select(stat)
# except Exception as e:
#     print('state 270', str(e))
#     stat = browser.find_element("id", "ctl00_ContentPlaceHolder1_ddlPState")
#     statt = Select(stat)

# print('state Options loading')
# print('state', state)
# # iterate over dropdown options
# for opt in statt.options:
#     print(opt.text)
#     if state.upper() in opt.text:
#         sel = Select(browser.find_element("id", 'ctl00_ContentPlaceHolder1_ddlPState'))

#         sel.select_by_visible_text(opt.text)
#         print(opt.text)
#         time.sleep(0.8)
#         break

# browser.implicitly_wait(15)

# try:
#     citya = browser.find_element("id", "ctl00_ContentPlaceHolder1_ddlPDistrict")
#     citys = Select(citya)
# except Exception as e:
#     print('citys 293', str(e))
#     citya = browser.find_element("id", "ctl00_ContentPlaceHolder1_ddlPDistrict")
#     citys = Select(citya)

# browser.implicitly_wait(15)
# print('city Options loading')
# print('city', district)
# # iterate over dropdown options
# for opt in citys.options:
#     print(opt.text)
#     if district.upper() in opt.text:
#         sel = Select(browser.find_element("id", 'ctl00_ContentPlaceHolder1_ddlPDistrict'))

#         sel.select_by_visible_text(opt.text)
#         print(opt.text)
#         time.sleep(0.8)
#         break

# browser.implicitly_wait(10)

# unitNewButton = WebDriverWait(browser, 5).until(
#         EC.element_to_be_clickable((By.ID, "ctl00_ContentPlaceHolder1_BtnPAdd")))
# unitNewButton.click()

# browser.implicitly_wait(13)

# try:
#     elementFlat = browser.find_element(By.ID, "ctl00_ContentPlaceHolder1_txtOffFlatNo")

#     actions = ActionChains(browser)
#     actions.move_to_element(elementFlat).perform()
#     print("Action324 ok")
# except Exception as e:
#     print('FlatNo 326', str(e))

# try:
#     time.sleep(5)
#     flatElement = WebDriverWait(browser, 10).until(
#             EC.presence_of_element_located((By.ID, "ctl00_ContentPlaceHolder1_txtOffFlatNo"))
#         ).send_keys(flat_no)

#     browser.find_element("id", "ctl00_ContentPlaceHolder1_txtOffFlatNo").send_keys(flat_no)
#     print("flat335 ok")
# except Exception as e:
#     print('flat 337', str(e))

# try:
#     browser.implicitly_wait(5)
#     browser.find_element("id", "ctl00_ContentPlaceHolder1_txtOffBuilding").send_keys(name_of_building)
# except Exception as e:
#     print('name_of_building 343', str(e))

# try:
#     browser.implicitly_wait(5)
#     browser.find_element("id", "ctl00_ContentPlaceHolder1_txtOffVillageTown").send_keys(village_town)
# except Exception as e:
#     print('village_town 349', str(e))

# try:
#     browser.implicitly_wait(5)
#     browser.find_element("id", "ctl00_ContentPlaceHolder1_txtOffBlock").send_keys(block)
# except Exception as e:
#     print('block 355', str(e))

# try:
#     browser.implicitly_wait(5)
#     browser.find_element("id", "ctl00_ContentPlaceHolder1_txtOffRoadStreetLane").send_keys(road_street)
# except Exception as e:
#     print('road_street 361', str(e))

# try:
#     time.sleep(2)
#     elementsFlat = browser.find_element(By.ID, "ctl00_ContentPlaceHolder1_txtOffCity")

#     actionsnew = ActionChains(browser)
#     actionsnew.move_to_element(elementsFlat).perform()

#     cityElement = WebDriverWait(browser, 10).until(
#         EC.presence_of_element_located((By.ID, "ctl00_ContentPlaceHolder1_txtOffCity"))
#     )

#     inputcity = browser.find_element("id", "ctl00_ContentPlaceHolder1_txtOffCity")
#     inputcity.send_keys(city)
# except Exception as e:
#     print('city 377', str(e))

# try:
#     browser.implicitly_wait(5)
#     browser.find_element("id", "ctl00_ContentPlaceHolder1_txtOffPin").send_keys(pincode)
# except Exception as e:
#     print('pincode 383', str(e))

# try:
#     browser.implicitly_wait(5)
#     stat = browser.find_element("id", "ctl00_ContentPlaceHolder1_ddlstate")
#     statt = Select(stat)
# except Exception as e:
#     print('state 390', str(e))
#     stat = browser.find_element("id", "ctl00_ContentPlaceHolder1_ddlstate")
#     statt = Select(stat)

# print('state Options loading')
# print('state', state)
# # iterate over dropdown options
# for opt in statt.options:
#     print(opt.text)
#     if state.upper() in opt.text:
#         sel = Select(browser.find_element("id", 'ctl00_ContentPlaceHolder1_ddlstate'))

#         sel.select_by_visible_text(opt.text)
#         print(opt.text)
#         time.sleep(0.8)
#         break

# browser.implicitly_wait(15)

# try:
#     city = browser.find_element("id", "ctl00_ContentPlaceHolder1_ddlDistrict")
#     citys = Select(city)
# except Exception as e:
#     print('citys 413', str(e))
#     city = browser.find_element("id", "ctl00_ContentPlaceHolder1_ddlDistrict")
#     citys = Select(city)

# browser.implicitly_wait(15)
# print('city Options loading')
# print('city', district)
# # iterate over dropdown options
# for opt in citys.options:
#     print(opt.text)
#     if district.upper() in opt.text:
#         sel = Select(browser.find_element("id", 'ctl00_ContentPlaceHolder1_ddlDistrict'))

#         sel.select_by_visible_text(opt.text)
#         print(opt.text)
#         time.sleep(0.8)
#         break

# try:
#     browser.find_element("id", "ctl00_ContentPlaceHolder1_txtdateIncorporation").send_keys(business_date)
# except Exception as e:
#     print('ex 434', str(e))

# try:
#     browser.find_element("id", "ctl00_ContentPlaceHolder1_txtcommencedate").send_keys(business_date)
# except Exception as e:
#     print('439', str(e))

# try:
#     browser.implicitly_wait(3)
#     browser.find_element("id", "ctl00_ContentPlaceHolder1_txtBankName").send_keys(bank_name)
# except Exception as e:
#     print('ex 445', str(e))

# try:
#     browser.find_element("id", "ctl00_ContentPlaceHolder1_txtaccountno").send_keys(account_number)
# except Exception as e:
#     print('ex 450', str(e))

# try:
#     browser.find_element("id", "ctl00_ContentPlaceHolder1_txtifsccode").send_keys(ifsc_code)
# except Exception as e:
#     print('ex 455', str(e))

# try:
#     bus_for = browser.find_element(By.XPATH,
#                                    "//td//label[contains( text( ), '" + business_activity + "')]").get_attribute('for')
#     actfield = browser.find_element(By.CSS_SELECTOR, '#' + bus_for)
#     browser.execute_script("arguments[0].click();", actfield)
# except Exception as e:
#     print('gender 463', str(e))

# try:
#     time.sleep(3)
#     maleElement = WebDriverWait(browser, 10).until(
#         EC.presence_of_element_located((By.ID, "ctl00_ContentPlaceHolder1_txtNoofpersonMale"))
#     )
#     browser.find_element("id", "ctl00_ContentPlaceHolder1_txtNoofpersonMale").send_keys(male_employees)
# except Exception as e:
#     print('ex 472', str(e))

# try:
#     browser.find_element("id", "ctl00_ContentPlaceHolder1_txtNoofpersonFemale").send_keys(female_employees)
# except Exception as e:
#     print('ex 477', str(e))

# try:
#     browser.find_element("id", "ctl00_ContentPlaceHolder1_txtNoofpersonOthers").send_keys(0)
# except Exception as e:
#     print('ex 482', str(e))

# try:
#     browser.find_element("id", "ctl00_ContentPlaceHolder1_txtDepCost").send_keys(0)
# except Exception as e:
#     print('ex 487', str(e))

# try:
#     browser.find_element("id", "ctl00_ContentPlaceHolder1_txtExCost").send_keys(0)
# except Exception as e:
#     print('ex 492', str(e))

# try:
#     browser.find_element("id", "ctl00_ContentPlaceHolder1_txtTotalTurnoverA").send_keys(0)
# except Exception as e:
#     print('ex 497', str(e))

# try:
#     actfield = browser.find_element(By.CSS_SELECTOR, '#ctl00_ContentPlaceHolder1_rbtPh_1')
#     browser.execute_script("arguments[0].click();", actfield)
# except Exception as e:
#     print('actfield 503', str(e))

# # unknown values
# try:
#     actfieldone = browser.find_element(By.CSS_SELECTOR, '#ctl00_ContentPlaceHolder1_rblGeM_1')
#     browser.execute_script("arguments[0].click();", actfieldone)
# except Exception as e:
#     print('actfield 510', str(e))

# try:
#     actfieldtwo = browser.find_element(By.CSS_SELECTOR, '#ctl00_ContentPlaceHolder1_rblTReDS_1')
#     browser.execute_script("arguments[0].click();", actfieldtwo)
# except Exception as e:
#     print('actfield 516', str(e))

# try:
#     actfieldthree = browser.find_element(By.CSS_SELECTOR, '#ctl00_ContentPlaceHolder1_rblNCS_1')
#     browser.execute_script("arguments[0].click();", actfieldthree)
# except Exception as e:
#     print('actfield 522', str(e))

# browser.find_element("id", "ctl00_ContentPlaceHolder1_btnsubmit").send_keys(Keys.ENTER)

browser.execute_script("alert('process completed')")

print('Process completed')
time.sleep(500)

print(name, email, mobile, aadhaar)
