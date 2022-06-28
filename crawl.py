from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import random

#Set up browser
browser = webdriver.Chrome(executable_path="chromedriver.exe")

#Set up post
browser.get("https://www.facebook.com/NHVLCN/posts/pfbid0erkNtmoP9wvqAk7bbo8XJwWyNb9ybeuPJkA4U5L7EWFoTUuZjB3y77WkLEZj9k4yl")
sleep(random.randint(3,5))

#Login

userId = browser.find_element_by_id("email")
userPass = browser.find_element_by_id("pass")
userId.send_keys("longlaninja@gmail.com")
userPass.send_keys("()Feed-AFK35")
submitButton = browser.find_element_by_id("loginbutton")
submitButton.click()
sleep(5)

#Ignore alert
option = Options()
option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")
# Pass the argument 1 to allow and 2 to block
option.add_experimental_option(
    "prefs", {"profile.default_content_setting_values.notifications": 1}
)
browser = webdriver.Chrome(
    chrome_options=option, executable_path=".\chromedriver.exe"
)


#Comments
showcomment_link = browser.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div[2]/div/div/div/div/div/div/div/div/div[2]/div[2]/form/div/div[2]/div[1]/div/div[3]/span[1]/a")
showcomment_link.click()
sleep(5)

#Reaction windows

#reactButton = browser.find_element_by_xpath("")
#reactButton.click()

#Close browser
browser.close()





