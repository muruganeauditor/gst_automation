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

import json

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

trnno_new = '332200277052TRN'

# private limited
responseData = '{"data":[{"id":19,"reg_taxtype":"APLRG","reg_state":"TAMIL NADU","reg_district":"Krishnagiri","reg_business_name":"EAUDITOR OFFICE PRIVATE LIMITED","reg_email":"muruganaccetcse@gmail.com","reg_mobile":"9585393730","reg_pan_number":"AAGCE3777M","trade_name":"eAuditor Business","constitution_business":"PVT","registration_reason":"VOLN","business_date":"2022-02-10","business_activity":"Manufacturing","trn_number":null,"hsn_code":"48205000","status":"1","created_at":"2022-11-25T13:25:45.883000Z","updated_at":"2022-11-25T13:28:28.827000Z","promotors":[{"id":7,"gst_form_id":"19","firstname":"Sathish","middlename":null,"lastname":"Ramalingam","designation_status":"Director","dob":"1997-03-10","personal_email":"muruganaccetcse@gmail.com","personal_mobile":"9585393730","gender":"Male","father_firstname":"Ramalingam","father_lastname":null,"residential_state":"Tamil Nadu","residential_district":"Krishnagiri","residential_city":"Pattanur","residential_locality":null,"residential_street":null,"residential_building_flat":null,"residential_landmark":null,"residential_pincode":null,"also_authorized_signatory":"Yes","profile_picture":"19-images.jpg","trn_number":null,"pan_number":"CLNPM9204L","din_number":"12345679" ,"status":"0","created_at":"2022-11-25T13:27:01.743000Z","updated_at":"2022-11-25T13:27:01.743000Z"},{"id":8,"gst_form_id":"19","firstname":"Murugan2","middlename":null,"lastname":"Palani2","designation_status":"Director","dob":"1998-02-10","personal_email":"muruganaccetcse2@gmail.com","personal_mobile":"9585393731","gender":"Male","father_firstname":"Dev","father_lastname":null,"residential_state":"Tamil Nadu","residential_district":"Krishnagiri","residential_city":"Pattanur","residential_locality":null,"residential_street":null,"residential_building_flat":null,"residential_landmark":null,"residential_pincode":null,"also_authorized_signatory":"No","profile_picture":"19-images.jpg","trn_number":null,"pan_number":"ABCTY1234D","din_number":"12345678" ,"status":"0","created_at":"2022-11-25T13:27:01.743000Z","updated_at":"2022-11-25T13:27:01.743000Z"}],"businesses":[{"id":6,"gst_form_id":"19","business_state":"Tamil Nadu","business_district":"Krishnagiri","business_city":"Selam","business_locality":null,"business_street":null,"business_building_flat":null,"business_landmark":null,"business_pincode":null,"state_jurisdiction_circle":null,"nature_profession":"REN","naturebusact":"LBU, RBU","trn_number":null,"principal_status":"1","status":"1","created_at":"2022-11-25T13:27:44.533000Z","updated_at":"2022-11-25T13:27:44.533000Z","proofs":[{"id":5,"gst_form_id":"19","gst_form_address_id":"6","business_place_proof":"RLAT","address_proof":"19-RLATdownload.jpg","status":"1","created_at":"2022-11-25T13:27:44.547000Z","updated_at":"2022-11-25T13:27:44.547000Z"},{"id":6,"gst_form_id":"19","gst_form_address_id":"6","business_place_proof":"ELCB","address_proof":"19-RLATdownload.jpg","status":"1","created_at":"2022-11-25T13:27:44.547000Z","updated_at":"2022-11-25T13:27:44.547000Z"}]}]}],"status":"true"}'

# Proprietor
# responseData = '{"data":[{"id":19,"reg_taxtype":"APLRG","reg_state":"TAMIL NADU","reg_district":"Krishnagiri","reg_business_name":"Palani Murugan","reg_email":"muruganaccetcse@gmail.com","reg_mobile":"9585393730","reg_pan_number":"CLNPM9204L","trade_name":"ABCD Business","constitution_business":"PRO","registration_reason":"VOLN","business_date":"2022-02-09","business_activity":"Manufacturing","trn_number":null,"hsn_code":"48205000","status":"1","created_at":"2022-11-25T13:25:45.883000Z","updated_at":"2022-11-25T13:28:28.827000Z","promotors":[{"id":7,"gst_form_id":"19","firstname":"Murugan","middlename":null,"lastname":"Palani","designation_status":"Proprietor","dob":"1997-03-10","personal_email":"muruganaccetcse@gmail.com","personal_mobile":"9585393730","gender":"Female","father_firstname":"Davidlee","father_lastname":null,"residential_state":"Tamil Nadu","residential_district":"Krishnagiri","residential_city":"Pattanur","residential_locality":null,"residential_street":null,"residential_building_flat":null,"residential_landmark":null,"residential_pincode":null,"also_authorized_signatory":"Yes","profile_picture":"19-images.jpg","trn_number":null,"status":"0","created_at":"2022-11-25T13:27:01.743000Z","updated_at":"2022-11-25T13:27:01.743000Z"}],"businesses":[{"id":6,"gst_form_id":"19","business_state":"Tamil Nadu","business_district":"Krishnagiri","business_city":"Selam","business_locality":null,"business_street":null,"business_building_flat":null,"business_landmark":null,"business_pincode":null,"state_jurisdiction_circle":null,"nature_profession":"REN","naturebusact":"LBU, RBU","trn_number":null,"principal_status":"1","status":"1","created_at":"2022-11-25T13:27:44.533000Z","updated_at":"2022-11-25T13:27:44.533000Z","proofs":[{"id":5,"gst_form_id":"19","gst_form_address_id":"6","business_place_proof":"RLAT","address_proof":"19-RLATdownload.jpg","status":"1","created_at":"2022-11-25T13:27:44.547000Z","updated_at":"2022-11-25T13:27:44.547000Z"},{"id":6,"gst_form_id":"19","gst_form_address_id":"6","business_place_proof":"ELCB","address_proof":"19-RLATdownload.jpg","status":"1","created_at":"2022-11-25T13:27:44.547000Z","updated_at":"2022-11-25T13:27:44.547000Z"}]}]}],"status":"true"}'

userDataResponse = json.loads(responseData)

userData = userDataResponse['data'][0]


print("login process will begin here")

if trnno_new != '':
    login.login_process(trnno_new, userData)
