from multiprocessing.resource_sharer import stop
from tracemalloc import start
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import timeit

# driver init
PATH= 'C:\TestFiles\chromedriver.exe'
driver = webdriver.Chrome(executable_path=PATH)
start = timeit.default_timer()
driver.get("https://www.amazon.pl/")

#close cookie
cookie_button = driver.find_element(By.ID, 'sp-cc-accept')
cookie_button.click()

#find search input field and locate search button to enter query
search_input = driver.find_element(By.ID, 'twotabsearchtextbox')
search_input.send_keys('iphone xr')
search_button = driver.find_element(By.ID, 'nav-search-submit-button')
search_button.click()

results = driver.find_elements(By.XPATH, '//*[@data-component-type = "s-search-result"]')

for result in results:
    title = driver.find_element(By.XPATH, '//*[contains(@class, "a-size-base-plus a-color-base a-text-normal")]').text
    price = driver.find_element(By.XPATH, '//*[@class = "a-price"]').text
    link = driver.find_element(By.XPATH, '//*[contains(@class, "a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal")]').get_attribute('href')

    print(title)
    print(price)
    print(link)

stop = timeit.default_timer()
print('Time: ', stop - start)


