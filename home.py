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

driver.get('http://practice.automationtesting.in/')
driver.implicitly_wait(10)
driver.execute_script('window.scrollBy(0,600);')
sel_ruby = driver.find_element_by_css_selector("[title='Selenium Ruby']")
sel_ruby.click()

reviews_tab = driver.find_element_by_class_name('reviews_tab')
reviews_tab.click()
five_star = driver.find_element_by_class_name('star-5')
five_star.click()
driver.find_element_by_id('comment').send_keys("Nice book!")
name = driver.find_element_by_id('author')
name.send_keys("Name")
email = driver.find_element_by_id('email')
email.send_keys('email@ya.com')
submit = driver.find_element_by_id('submit')
submit.click()