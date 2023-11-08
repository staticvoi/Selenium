#import selenium
from selenium import webdriver
import pandas as pd

df = pd.read_excel (r'C:\Users\HP\Desktop\Selenium using python\data.xlsx')
#print (df)

#for login using pandas
name = df.iloc[0][0]
psw = df.iloc[0][1]


PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
#print(driver.title)
#print(driver.page_source)



#using pandas for github
driver.get('https://github.com/login')

username_text = driver.find_element_by_id("login_field").send_keys(name)

password_text = driver.find_element_by_id("password").send_keys(psw)

login = driver.find_element_by_name("commit").click()

#driver.save_screenshot(r'C:\Users\HP\Desktop\Selenium using python\github.png') #can take png,jpg etc
driver.get_screenshot_as_file(r'C:\Users\HP\Desktop\Selenium using python\github1.png') #takes only png


#driver.close() #closes tab
#driver.quit()  #closes browser
