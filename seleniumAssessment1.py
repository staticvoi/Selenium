#import selenium
from selenium import webdriver
import pandas as pd
from getpass import getpass
import time
from selenium.webdriver.chrome.options import Options

#for direct login
username = input("Enter username: ")
password = getpass("Enter password: ") #works only on terminal


PATH = "C:\Program Files (x86)\chromedriver.exe"

options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(PATH, options=options)

#driver = webdriver.Chrome(PATH)
#driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\chromedriver.exe")


#driver.get('https://google.com')
#driver.maximize_window()
#print(driver.title)
#print(driver.page_source)

#for fb
#driver.get('https://www.facebook.com/') 

#username_text = driver.find_element_by_id("email")
#username_text.send_keys(username)

#password_text = driver.find_element_by_id("pass")
#password_text.send_keys(password)

#login = driver.find_element_by_id("loginbutton")
#login.click()


#for github
driver.get('https://github.com/login')
driver.maximize_window()

time.sleep(5)

username_text = driver.find_element_by_id("login_field").send_keys(username)
#driver.find_element_by_xpath("/html/body/div[4]/div/div/div/main/div[1]/div/div/a[1]")
time.sleep(5)

password_text = driver.find_element_by_id("password").send_keys(password)
time.sleep(5)

login = driver.find_element_by_name("commit").click()
time.sleep(5)
#login = driver.find_element_by_name("commit").submit()

print("Login done")


driver.close() #closes tab
#driver.quit()  #closes browser
