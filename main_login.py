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

trnno_new = '332200269210TRN'

print("login process will begin here")

if trnno_new != '':
    login.login_process(trnno_new)
