from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get("https://www.google.com/")

searchBox = driver.find_element(By.NAME,"q")
searchBox.send_keys("Aamaey Prakash")
searchBox.send_keys(Keys.RETURN)



input("Press any key to close it")
driver.quit()