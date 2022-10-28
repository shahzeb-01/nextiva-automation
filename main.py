from time import sleep
from selenium import webdriver
import winsound
from csv import DictWriter
import csv
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
# print("before sleep")
# sleep(2100)
# print("After sleep")
import pdb

opp = Options()
prefs = {'profile.default_content_setting_values': { 'images': 2,
                                                    'plugins': 2, 'popups': 2, 'geolocation': 2,
                                                    'notifications': 2, 'auto_select_certificate': 2, 'fullscreen': 2,
                                                    'mouselock': 2, 'mixed_script': 2, 'media_stream': 2,
                                                    'media_stream_mic': 2, 'media_stream_camera': 2, 'protocol_handlers': 2,
                                                    'ppapi_broker': 2, 'automatic_downloads': 2, 'midi_sysex': 2,
                                                    'push_messaging': 2, 'ssl_cert_decisions': 2, 'metro_switch_to_desktop': 2,
                                                    'protected_media_identifier': 2, 'app_banner': 2, 'site_engagement': 2,
                                                    'durable_storage': 2}}
opp.add_experimental_option('prefs', prefs)
opp.add_argument("start-minimized")
opp.add_argument("--disable-notifications")
opp.add_argument("disable-infobars")
opp.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 1})
opp.binary_location = "C:\Program Files\Google\Chrome Beta\Application\chrome.exe"
# opp.add_argument("--headless")
opp.add_argument("--disable-extensions")
opp.add_argument('--blink-settings=imagesEnabled=false')
browser = webdriver.Chrome('chromedriver', options=opp)


# def read_data_from_csv():
#     with open('event.csv', 'a', newline='') as outputfile:
#         header = ['Name', 'Phone Number', 'State', 'NPI No.', 'Speciality']
#         writer = csv.writer(outputfile)
#         writer.writerow(header)
#     file = open("npi.csv", "r")
#     csv_reader = csv.reader(file)
#     lists_from_csv = []
#     for row in csv_reader:
#         lists_from_csv.append(row)
#     flat_list = []
#     for sublist in lists_from_csv:
#         for item in sublist:
#             flat_list.append(item)
#     print("*******************************************")
#     print(len(flat_list), " Total Contacts")
#     print("*******************************************")

#     for num in flat_list:
#         inx = flat_list.index(num)
#         print(inx, " = ", num)

#         try:
#             get_data_from_web(num)

#         except:
#             # if not has_connection():
#             #     print('No Internet connection, aborted!')
#             #     browser.quit()
#             #     winsound.PlaySound("bell.wav", winsound.SND_FILENAME)
#             #     exit()
#             #     break
#             pass
#     # Clean()
#     # browser.quit()

def get_data_from_web():
    url = "https://ezmdsolutions.nextos.com/apps/home/#/user/"

    browser.get(url)
    WebDriverWait(browser, 7).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="username"]')))

    username = browser.find_element(
        By.XPATH, value='//*[@id="username"]').send_keys("david@ezmdsolutions.com")
        
    browser.find_element(By.XPATH, value='//*[@id="idp-discovery-submit"]').click()

    WebDriverWait(browser, 7).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="password"]')))

    password = browser.find_element(
        By.XPATH, value='//*[@id="password"]').send_keys("Team12345$")

    browser.find_element(By.XPATH, value='//*[@id="nextiva-login-form"]/button').click()
    WebDriverWait(browser, 7).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="react-mount-point"]/div/div/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div[1]/div/div/button[2]')))
    browser.find_element(By.XPATH, value='//*[@id="react-mount-point"]/div/div/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div[1]/div/div/button[2]').click()
    sleep(15)
    
    browser.switch_to.default_content()

    sleep(20)
    browser.find_element(By.XPATH, value='//*[@id="create-actions"]').click()
    WebDriverWait(browser, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div[3]/ul/div[1]/li[2]')))

    browser.find_element(By.XPATH, value='/html/body/div[2]/div[3]/ul/div[1]/li[2]').click()
    pdb.set_trace()
    browser.find_element(By.XPATH, value='//*[@id="nextiva-one-content-container"]/div[2]/div/div/div[1]/div/div').click()
    input = browser.find_element(By.XPATH, value='//*[@id="nextiva-one-content-container"]/div[2]/div/div/div[1]/div/div').send_keys("6093319091")
    input.send_keys(Keys.ENTER)
    sleep(5)
   
    msg=browser.find_element(By.XPATH, value='//*[@id="nextiva-one-content-container"]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div[1]/div/textarea[1]').send_keys("Team12345$")

    msg.send_keys(Keys.ENTER)
    


if __name__ == "__main__":
    get_data_from_web()
