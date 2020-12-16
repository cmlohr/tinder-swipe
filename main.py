from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
import time

WEB_PAGE = "https://tinder.com/app/recs"
DRIVER_PATH = "YOUR_DRIVER_PATH"
GOOGLE_EMAIL = "YOUR_LOGIN_EMAIL"
GOOGLE_PASS = "YOUR_PASSWORD"
# xpaths of login and like btns moved into consts for length and better readability
LOGIN_BTN = '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/button'
LIKE_BTN = '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button'

# get webpage
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get(WEB_PAGE)
print("webpage loaded")

# begin login flow
time.sleep(1)
login = driver.find_element_by_xpath(LOGIN_BTN)
login.click()
print('>>> click login')

# set for google login for personal preference
time.sleep(1)
google_login = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[1]/div/button')
google_login.click()
print(f"Checkpoint 1: {driver.title}")

# move to login window
time.sleep(4)
tinder_main = driver.window_handles[0]
google_login_window = driver.window_handles[1]
driver.switch_to.window(google_login_window)
print(f"Checkpoint 2: {driver.title}")
print(">>> logging in...")

# enter credentials 1: email
time.sleep(2)
google_email_input = driver.find_element_by_xpath('//*[@id="identifierId"]')
google_email_input.send_keys(GOOGLE_EMAIL)
google_email_input.send_keys(Keys.ENTER)
print(">>> email accepted")

# enter credentials 2: password
time.sleep(2)
google_pass_input = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
google_pass_input.send_keys(GOOGLE_PASS)
google_pass_input.send_keys(Keys.ENTER)
print(">>> password accepted")

# wait for verification, as 2fa is turned on for the account used
print("wait...")
time.sleep(5)  # may need to be set longer for longer 2fa verificaiton window
driver.switch_to.window(tinder_main)
print(f"Checkpoint 3: {driver.title}")
print(">>> signed in")

# click through popups:  cookies accept
time.sleep(1)
cookie_accept = driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
cookie_accept.click()
print(">>> accepted cookies")

# click through popups:  accept location
print("wait...")
time.sleep(5)
location_allow = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
location_allow.click()
print(">>> allowed location")

# click through popups:  deny notifications
time.sleep(2)
notification_dismiss = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/button[2]')
notification_dismiss.click()
print(">>> dismiss notifications")

# wait for webpage loading
time.sleep(2)
print(f"Checkpoint 4: {driver.title}")
print('wait...')
time.sleep(4)
print('two sec delay btw swipes')

# begin hitting like for 100 (free account) likes
for tries in range(100):
    try:
        time.sleep(2)
        like_button = driver.find_element_by_xpath(LIKE_BTN)
        like_button.click()
        print('swipe')
    except ElementClickInterceptedException:
        try:
            # got a match exception
            print('got a match')
            got_a_match = driver.find_element_by_css_selector(".itsAMatch a")
            got_a_match.click()
            print('match cleared')
        except NoSuchElementException:
            # no such element exception
            print('no such element exception')
            time.sleep(3)

# passing 'pass' through except and finally - skipping the exceptions allows user control of popups
# as showing in the code below
# for tries in range(100):
#     try:
#         time.sleep(2)
#         like_button = driver.find_element_by_xpath(like)
#         like_button.click()
#         print('swipe')
#     except:
#         pass
#     finally:
#         pass

driver.quit()
