from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import timeit
import time
import pandas as pd


class Amazoncrawler(object):
    def __init__(self) -> None:
        self.options = Options()
        self.driver = webdriver.Chrome(service=Service('C:\TestFiles\chromedriver.exe'), options=self.options)
        self.driver.implicitly_wait(5)
        products_title = []
        products_price = []
        products_link = []
        templist = []

    def driver_quit(self):
        self.driver.quit()
    
    def main_page(self):
        self.driver.get("https://www.amazon.pl/")

        #close cookie
        try:
            cookie_button = self.driver.find_element(By.ID, 'sp-cc-accept')
            cookie_button.click()
        except:
            pass
    
    def search(self):
        search_input = self.driver.find_element(By.ID, 'twotabsearchtextbox')
        query = input('Amazon search: ')
        search_input.send_keys(query)
        search_button = self.driver.find_element(By.ID, 'nav-search-submit-button')
        search_button.click()
    
    def locate_elements(self):
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        results = WebDriverWait(self.driver,10).until(
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
                
                self.templist.append(Table_dict)
            except:
                pass

    def pagination(self):
        pass

    def csv_export(self):
        pass