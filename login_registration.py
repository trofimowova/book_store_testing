from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

path_to_extension = r'C:\Users\Vladimir\AppData\Local\Google\Chrome\User Data\Default\Extensions\gighmmpiobklfepjocnamgkkbiglidom\4.34.0_0'
chrome_options = Options()
chrome_options.add_argument('load-extension=' + path_to_extension)
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.create_options()
time.sleep(10)
driver.maximize_window()
driver.implicitly_wait(5)
first_browser_tab = driver.window_handles[0]
driver.switch_to.window(first_browser_tab)
"""
driver.get('http://practice.automationtesting.in/')
my_acc = driver.find_element_by_id('menu-item-50')
my_acc.click()

email = 'vov2@ya.ru'
driver.find_element_by_id('reg_email').send_keys(email)

passw_1 = 'H@ZDwvq1211'
driver.find_element_by_id('reg_password').send_keys(passw_1)
WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[name='register']"))).click()
"""
#-------------------------------------------------------------
#

driver.get(' http://practice.automationtesting.in/')
my_acc = driver.find_element_by_id('menu-item-50')
my_acc.click()

email = 'vov2@ya.ru'
driver.find_element_by_id('username').send_keys(email)

passw_1 = 'H@ZDwvq1211'
driver.find_element_by_id('password').send_keys(passw_1)

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[name='login']"))).click()
if (EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'Logout'))):
    print(f'Element "Logout" is detected')