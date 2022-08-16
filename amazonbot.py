from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# driver init
PATH= 'C:\TestFiles\chromedriver.exe'
driver = webdriver.Chrome(executable_path=PATH)
driver.get("https://www.amazon.pl/")

#close cookie
cookie_button = driver.find_element(By.ID, 'sp-cc-accept')
cookie_button.click()

#find search input field and locate search button to enter query
search_input = driver.find_element(By.ID, 'twotabsearchtextbox')
search_input.send_keys('iphone xr')
search_button = driver.find_element(By.ID, 'nav-search-submit-button')
search_button.click()

