from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import timeit
import time
import pandas as pd

templist = []

def locate_elements():
    time.sleep(2)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    results = WebDriverWait(driver,10).until(
        EC.presence_of_all_elements_located((By.XPATH, '//div[contains(@class, "s-result-item s-asin")]')))
    for result in results:
        try:
            title = result.find_element(By.XPATH, './/h2[contains(@class, "a-color-base")]')
            price = result.find_element(By.XPATH, './/*[@class = "a-price"]')
            link = result.find_element(By.XPATH, './/*[contains(@class, "a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal")]').get_attribute("href")
        except:
            title = 'NULL'
            price = 'NULL'
            link = 'NULL'
            
        try:
            Table_dict={ 'title': title.text,
                    'price': price.text,
                    'link': link}
            
            templist.append(Table_dict)
        except:
            pass


# driver init
PATH= 'C:\TestFiles\chromedriver.exe'
driver = webdriver.Chrome(executable_path=PATH)
start = timeit.default_timer()
driver.get("https://www.amazon.pl/")

#close cookie
try:
    cookie_button = driver.find_element(By.ID, 'sp-cc-accept')
    cookie_button.click()
except:
    pass

#find search input field and locate search button to enter query
search_input = driver.find_element(By.ID, 'twotabsearchtextbox')
search_input.send_keys('iphone xr')
search_button = driver.find_element(By.ID, 'nav-search-submit-button')
search_button.click()

number_of_pages = int(driver.find_element(By.XPATH, '//*[contains(@class, "s-pagination-item s-pagination-disabled")]').text)
while number_of_pages-1 >= 0:
    locate_elements()
    next_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[text() = "Dalej"]')))
    next_button.click()
    number_of_pages -=1


df = pd.DataFrame(templist)
df.to_csv('table.csv') 
# driver.close()

stop = timeit.default_timer()
print('Time: ', stop - start)
