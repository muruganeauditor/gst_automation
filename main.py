import string
import sys
import requests
import datetime
import login
import json

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

api_url = "http://admin.ibuyfresh.in/api/udyamDetails"
response = requests.get(api_url)
apiResponse = response.json()
# print(apiResponse['status'])

if apiResponse['status']:
    if len(apiResponse['data'])>0:
        userData = apiResponse['data'][0]
        locals().update(userData)
else:
    print("Invalid Api response")
    sys.exit()

responseData = '{"data":[{"id":19,"reg_taxtype":"APLRG","reg_state":"TAMIL NADU","reg_district":"Krishnagiri","reg_business_name":"Palani Murugan","reg_email":"muruganaccetcse@gmail.com","reg_mobile":"9585393730","reg_pan_number":"CLNPM9204L","trade_name":"Murugan Palani","constitution_business":"PRO","registration_reason":"VOLN","business_date":"2022-02-09","business_activity":"Manufacturing","trn_number":null,"hsn_code":"48205000","status":"1","created_at":"2022-11-25T13:25:45.883000Z","updated_at":"2022-11-25T13:28:28.827000Z","promotors":[{"id":7,"gst_form_id":"19","firstname":"Murugan","middlename":null,"lastname":"Palani","designation_status":"Proprietor","dob":"1998-02-10","personal_email":"muruganaccetcse@gmail.com","personal_mobile":"9585393730","gender":"Male","father_firstname":"Palani","father_lastname":null,"residential_state":"Tamil Nadu","residential_district":"Krishnagiri","residential_city":"Pattanur","residential_locality":null,"residential_street":null,"residential_building_flat":null,"residential_landmark":null,"residential_pincode":null,"also_authorized_signatory":"Yes","profile_picture":"19-images.jpg","trn_number":null,"status":"0","created_at":"2022-11-25T13:27:01.743000Z","updated_at":"2022-11-25T13:27:01.743000Z"}],"businesses":[{"id":6,"gst_form_id":"19","business_state":"Tamil Nadu","business_district":"Krishnagiri","business_city":"Selam","business_locality":null,"business_street":null,"business_building_flat":null,"business_landmark":null,"business_pincode":null,"state_jurisdiction_circle":null,"nature_profession":"REN","naturebusact":"LBU, RBU","trn_number":null,"principal_status":"1","status":"1","created_at":"2022-11-25T13:27:44.533000Z","updated_at":"2022-11-25T13:27:44.533000Z","proofs":[{"id":5,"gst_form_id":"19","gst_form_address_id":"6","business_place_proof":"RLAT","address_proof":"19-RLATdownload.jpg","status":"1","created_at":"2022-11-25T13:27:44.547000Z","updated_at":"2022-11-25T13:27:44.547000Z"}]}]}],"status":"true"}'

userDataResponse = json.loads(responseData)

userData = userDataResponse['data'][0]

browser = webdriver.Chrome(service=Service('C:\\Users\\Liva\\Desktop\\gst_automation\\chromedriver.exe'))

browser.maximize_window()
browser.get("https://reg.gst.gov.in/registration/")

browser.implicitly_wait(5)

# userData = {}
# userData['email'] = 'murugan@eauditoroffice.com'
# userData['mobile'] = '9585393730'
# userData['pan_number'] = 'BLEPN5033N'
# userData['business_name'] = 'Rajan Nithyakala'
# userData['taxtype'] = 'APLRG'
# userData['state'] = 'Tamil Nadu'
# userData['district'] = 'Coimbatore'
# userData['trade_name'] = 'ABC Company'
# userData['constitution_business'] = 'PRO'
# userData['registration_reason'] = 'VOLN'
# userData['business_date'] = '2002-05-10'
# userData['father_firstname'] = 'Rajan'
# userData['father_lastname'] = 'Raj'
# userData['dob'] = '1990-05-10'
# userData['gender'] = 'Female'
# userData['designation_status'] = 'Proprietor'
# userData['also_authorized_signatory'] = 'Yes'
# userData['state_jurisdiction_circle'] = ''
# userData['commissionerate'] = ''
# userData['division'] = ''
# userData['range'] = ''
# userData['nature_profession'] = 'CON'
# userData['proof'] = { '0': {'CNLR': 'C:\\Users\\Murugan\\Desktop\\download.jpg'},
#                       '1': {'ELCB': 'C:\\Users\\Murugan\\Desktop\\download.jpg'}}
#
#
#
# format = '%Y-%m-%d'
# datetime = datetime.datetime.strptime(userData['business_date'], format)
# userData['business_date'] = datetime.date().strftime("%d%m%Y")
#
# datetimedob = datetime.datetime.strptime(userData['dob'], format)
# userData['dob'] = datetimedob.date().strftime("%d%m%Y")



try:
    print("inside tax")
    sel = Select(browser.find_element("id", 'applnType'))

    sel.select_by_value(userData['reg_taxtype'])

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
    # print(userData['reg_state'], opt.text)
    if userData['reg_state'].upper() in (opt.text).upper():
        sel = Select(browser.find_element("id", 'applnState'))

        sel.select_by_visible_text(opt.text)
        print(opt.text)
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
    if userData['reg_district'].upper() in (opt.text).upper():
        sel = Select(browser.find_element("id", 'applnDistr'))

        sel.select_by_visible_text(opt.text)
        print(opt.text)
        time.sleep(0.8)
        break

browser.implicitly_wait(15)

try:
    browser.find_element("id", "bnm").send_keys(userData['reg_business_name'])
except Exception as e:
    print('state 61', str(e))


try:
    browser.find_element("id", "pan_card").send_keys(userData['reg_pan_number'])
except Exception as e:
    print('state 61', str(e))


try:
    browser.implicitly_wait(2)
    browser.find_element("id", "email").send_keys(userData['reg_email'])
except Exception as e:
    print('ex 74', str(e))

try:
    mobileElement = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.ID, "mobile"))
    )
    browser.find_element("id", "mobile").send_keys(userData['reg_mobile'])
except Exception as e:
    print('ex 82', str(e))

try:
    browser.execute_script("window.scrollTo(0, 100)")
except Exception as e:
    print('ex 82', str(e))

try:
    mobileElement = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.ID, "captcha"))
    )
    browser.find_element("id", "captcha").send_keys('')
except Exception as e:
    print('ex 82', str(e))


try:
    mobileElement = WebDriverWait(browser, 20).until(
        EC.presence_of_element_located((By.ID, "mobile_otp"))
    )
    browser.find_element("id", "mobile_otp").send_keys('')
except Exception as e:
    print('ex 181', str(e))

print(93, 'sleep')
time.sleep(30)
browser.implicitly_wait(50)
print(95, 'going to look alert')
try:
    elementPara = WebDriverWait(browser, 4000).until(
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
    browser.implicitly_wait(10)
    element = WebDriverWait(browser, 800).until(
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
    element = WebDriverWait(browser, 500).until(
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
browser.execute_script("$('form').append('<h1>This is from bot, please wait this window will close and new window will be opened!</h1>')")
# content = '<br><br><h1 style="color:red">This is from bot, please wait this window will close and new window will be opened!</h1><br><br>'
# browser.execute_script(f'$("form").append({content})')
# time.sleep(200)
#
print("login process will begin here")

try:
    if trnno_new != '':
        browser.close()
        browser.quit()
        login.login_process(trnno_new, userData)
except Exception as e:
    print("failed to login")

# print('Process completed')
# time.sleep(500)
