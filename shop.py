from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import keyboard

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
my_acc = driver.find_element_by_id('menu-item-50')
my_acc.click()
"""
email = 'vov2@ya.ru'
driver.find_element_by_id('username').send_keys(email)

passw_1 = 'H@ZDwvq1211'
driver.find_element_by_id('password').send_keys(passw_1)

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[name='login']"))).click()
shop_tab = driver.find_element_by_id('menu-item-40')
shop_tab.click()

html_5 = driver.find_element_by_css_selector("[title='Mastering HTML5 Forms']")
html_5.click()

if EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.product_title.entry-title'), 'HTML5 Forms'):
    print(f'Header is "HTML5 Forms"')
    
#-------------------------------------
 

#driver.get('http://practice.automationtesting.in/')
#my_acc = driver.find_element_by_id('menu-item-50')
#my_acc.click()

email = 'vov2@ya.ru'
driver.find_element_by_id('username').send_keys(email)

passw_1 = 'H@ZDwvq1211'
driver.find_element_by_id('password').send_keys(passw_1)

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[name='login']"))).click()
shop_tab = driver.find_element_by_id('menu-item-40')
shop_tab.click()

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'.cat-item-19 :nth-child(1)'))).click()



catalog_item = driver.find_element_by_class_name('type-product')

num_of_elem = driver.execute_script('(document.getElementsByClassName("type-product").length);')
print(num_of_elem)

driver.execute_script('var n = document.getElementsByClassName("type-product").length;if (n=3){alert(" На странице отображается 3 элемента")};')

#-----------------------------------------------------------------------------------------------------

email = 'vov2@ya.ru'
driver.find_element_by_id('username').send_keys(email)

passw_1 = 'H@ZDwvq1211'
driver.find_element_by_id('password').send_keys(passw_1)

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[name='login']"))).click()
shop_tab = driver.find_element_by_id('menu-item-40')
shop_tab.click()

if EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".orderby [selected='selected']"),'Default sorting'):
    print("Meaning of selector is DEFAULT")
sel_el = driver.find_element_by_css_selector(".orderby")
select = Select(sel_el)
select.select_by_visible_text("Sort by price: high to low")

sel_el = driver.find_element_by_css_selector(".orderby")
select = Select(sel_el)
select.select_by_value("price-desc")

if EC.presence_of_element_located((By.CSS_SELECTOR, ".orderby [value='price-desc']")):
    print("Sort by price: high to low")
#--------------------------------------------------------------

email = 'vov2@ya.ru'
driver.find_element_by_id('username').send_keys(email)

passw_1 = 'H@ZDwvq1211'
driver.find_element_by_id('password').send_keys(passw_1)

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[name='login']"))).click()
shop_tab = driver.find_element_by_id('menu-item-40')
shop_tab.click()
android = driver.find_element_by_css_selector("[title='Android Quick Start Guide']")
android.click()

old_price = driver.find_element_by_css_selector('.woocommerce-Price-amount.amount')
assert '₹600.00' in old_price.text

new_price = driver.find_element_by_css_selector('ins .woocommerce-Price-amount.amount')
assert '₹450.00' in new_price.text

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "img[alt='Android Quick Start Guide']"))).click()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, "pp_close"))).click()
driver.quit()
#-------------------------------------------------------------------------------------


email = 'vov2@ya.ru'
driver.find_element_by_id('username').send_keys(email)

passw_1 = 'H@ZDwvq1211'
driver.find_element_by_id('password').send_keys(passw_1)

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[name='login']"))).click()
shop_tab = driver.find_element_by_id('menu-item-40')
shop_tab.click()

add_to_btn=driver.find_element_by_css_selector('.post-182 .button')
add_to_btn.click()

item_num = driver.find_element_by_css_selector('.wpmenucart-contents .cartcontents')
print(item_num.text)
assert   "1 Item" in item_num.text
price_html = driver.find_element_by_css_selector('.wpmenucart-contents :nth-child(3)')
assert "₹180.00" in price_html.text

driver.find_element_by_css_selector(".wpmenucart-contents").click()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.cart-subtotal :nth-child(2) > span')))
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.order-total :nth-child(2) span')))

#-------------------------------------------------------------------------------------


shop_tab = driver.find_element_by_id('menu-item-40')
shop_tab.click()

add_to_btn_1 = driver.find_element_by_css_selector('.post-182 .button')
add_to_btn_1.click()
driver.execute_script("window.scrollBy(0,300);")
WebDriverWait(driver, 20).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,".cartcontents"), "1 Item"))
time.sleep(4)
add_to_btn_2 = driver.find_element_by_css_selector('.post-180 .button')
add_to_btn_2.click()

driver.find_element_by_css_selector(".wpmenucart-contents").click()
time.sleep(3)
driver.find_element_by_css_selector("[title='Remove this item']").click()
driver.find_element_by_link_text("Undo?").click()
time.sleep(4)
driver.find_element_by_css_selector('[name="cart[045117b0e0a11a242b9765e79cbf113f][qty]"]').clear()
driver.find_element_by_css_selector('[name="cart[045117b0e0a11a242b9765e79cbf113f][qty]"]').send_keys('3')

upd_bsk = driver.find_element_by_css_selector("[value='Update Basket']")
upd_bsk.click()

val = driver.find_element_by_css_selector('[name="cart[045117b0e0a11a242b9765e79cbf113f][qty]"]')
if (val.get_attribute('value')) == '3':
    print('Value is Correct')
time.sleep(3)
app_cop = driver.find_element_by_css_selector('.coupon :nth-child(3)')
app_cop.click()
if (EC.presence_of_element_located((By.CSS_SELECTOR,'.woocommerce-error li'))):
    print('message is located ')

"""
shop_tab = driver.find_element_by_id('menu-item-40')
shop_tab.click()

add_to_btn_1 = driver.find_element_by_css_selector('.post-182 .button')
add_to_btn_1.click()
driver.execute_script("window.scrollBy(0,300);")
add_to_btn_2 = driver.find_element_by_css_selector('.post-182 .button')
add_to_btn_2.click()
time.sleep(3)
driver.find_element_by_css_selector(".wpmenucart-contents").click()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.wc-proceed-to-checkout a'))).click()
driver.find_element_by_id("billing_first_name").send_keys("Hos")
driver.find_element_by_id("billing_last_name").send_keys("pital")
driver.find_element_by_id("billing_email").send_keys("hp@ya.ru")
driver.find_element_by_id("billing_phone").send_keys("123456789")

driver.find_element_by_class_name('select2-chosen').click()
country_input = driver.find_element_by_css_selector('.select2-search input')
country_input.send_keys("Reunion")
time.sleep(3)
driver.find_element_by_css_selector('.select2-results-dept-0.select2-result.select2-result-selectable')
#keyboard.send("Ctrl+Shift+C")

driver.find_element_by_id("billing_address_1").send_keys("Apartament6")
driver.find_element_by_id("billing_city").send_keys("Eco")
driver.find_element_by_id("billing_state").send_keys("State")
driver.find_element_by_id("billing_postcode").send_keys("billing_postcode")
driver.execute_script("window.scrollBy(0,600);")

#payment = driver.find_element_by_id('payment_method_cod')
#payment.click()
#time.sleep(5)
#place_order = driver.find_element_by_id('place_order')
#place_order.click()







