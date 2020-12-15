from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

WEB_PAGE = "https://tinder.com/app/recs"
DRIVER_PATH = "YOUR_DRIVER_PATH"

GOOGLE_EMAIL = "YOUR_LOGIN_EMAIL"
GOOGLE_PASS = "YOUR_PASSWORD"

driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get(WEB_PAGE)
print("web page loaded")
X = '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/button'

time.sleep(1)
login = driver.find_element_by_xpath(X)
login.click()

time.sleep(1)
google_login = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[1]/div/button')
google_login.click()
print(f"Checkpoint 1: {driver.title}")

time.sleep(2)
tinder_main = driver.window_handles[0]
google_login_window = driver.window_handles[1]
driver.switch_to.window(google_login_window)
print(f"Checkpoint 2: {driver.title}")
print(">>> logging in...")

time.sleep(2)
google_email_input = driver.find_element_by_xpath('//*[@id="identifierId"]')
google_email_input.send_keys(GOOGLE_EMAIL)
google_email_input.send_keys(Keys.ENTER)
print(">>> email accepted")

time.sleep(2)
google_pass_input = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
google_pass_input.send_keys(GOOGLE_PASS)
google_pass_input.send_keys(Keys.ENTER)
print(">>> password accepted")

print("wait...")
time.sleep(5)
driver.switch_to.window(tinder_main)
print(f"Checkpoint 3: {driver.title}")
print(">>> signed in")

time.sleep(1)
cookie_accept = driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
cookie_accept.click()
print(">>> accepted cookies")

print("wait...")
time.sleep(5)
location_allow = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
location_allow.click()
print(">>> allowed location")

time.sleep(2)
accept_msgs = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
accept_msgs.click()
print(">>> accept messages")

time.sleep(2)
print(f"Checkpoint 4: {driver.title}")
print('>Begin swipe<')

# TODO: Locate swipe XPATH
# TODO: POP UP EXCEPTIONS
#
# match = driver.find_element_by_xpath('') <<<<< need to trigger
# match.click()

# home_screen_popup = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
# home_screen_popup.click()
#
# out_of_likes = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/button[2]')
# out_of_likes.click()
# #quit here
