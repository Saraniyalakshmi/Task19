import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By

paths = r"C:\Users\Ranga\OneDrive\Desktop\chromedriver.exe"
os.environ["PATH"] += os.pathsep + os.path.dirname(paths)

chrome_options = Options()

chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
time.sleep(2)
driver.get("https://www.saucedemo.com/")
time.sleep(2)
driver.maximize_window()
username=driver.find_element(By.ID,"user-name")
time.sleep(4)
username.click()
time.sleep(2)
username.send_keys("standard_user")
passw=driver.find_element(By.ID,"password")
passw.click()
passw.send_keys("secret_sauce")
logins=driver.find_element(By.ID,"login-button")
logins.click()
print("Title of webpage:",driver.title)
print("Current URL of webpage:",driver.current_url)
file = open(r"C:\Users\MageSaran\PycharmProjects\FirstPythonproject\FirstPythonProject_May4\webpage_task11.txt", "x")
p=(driver.find_element(By.XPATH, value='//*[@id="root"]'))
file=open(r"C:\Users\MageSaran\PycharmProjects\FirstPythonproject\FirstPythonProject_May4\webpage_task11.txt", 'w')
file.write(p.text)
print("webpage_task11.txt file created successfully")
file.close()
time.sleep(2)
driver.close()


