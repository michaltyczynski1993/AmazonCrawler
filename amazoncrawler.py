from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


class Amazoncrawler(object):
    def __init__(self) -> None:
        self.options = Options()
        self.driver = webdriver.Chrome(service=Service('C:\TestFiles\chromedriver.exe'), options=self.options)
        self.driver.implicitly_wait(5)

    def driver_quit(self):
        self.driver.quit()
    
    def main_page(self):
        self.driver.get("https://www.amazon.pl/")

        #close cookie
        cookie_button = self.driver.find_element(By.ID, 'sp-cc-accept')
        cookie_button.click()

        #find search input field and locate search button to enter query
        search_input = self.driver.find_element(By.ID, 'twotabsearchtextbox')
        query = input('Amazon search: ')
        search_input.send_keys(query)
        search_button = self.driver.find_element(By.ID, 'nav-search-submit-button')
        search_button.click()