from bs4 import BeautifulSoup as Bs
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
import json




class Parser:
	URL = "https://www.avito.ru/sankt-peterburg/kvartiry/sdam/na_dlitelnyy_srok-ASgBAgICAkSSA8gQ8AeQUg?context=H4sIAAAAAAAA_0q0MrSqLraysFJKK8rPDUhMT1WyLrYyNLNSKk5NLErOcMsvyg3PTElPLVGyrgUEAAD__xf8iH4tAAAA"
	
	def get_url(self, driver: webdriver.Chrome):
		driver.get(self.URL)
		
		
	@staticmethod
	def start_pars(driver: webdriver.Chrome):
		html = driver.page_source
		soup = Bs(html, 'lxml')
		
		blok = soup.find('div', class_="items-items-kAJAg")
		elements = blok.select('.items-items-kAJAg > div')
		flats = list(map(lambda m: m if len(m.text) > 1 else elements.pop(elements.index(m)), elements))
		
		return flats
	
	@staticmethod
	def new_page(driver: webdriver.Chrome, wait: WebDriverWait):
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight - 1700);")
		wait.until(ec.visibility_of_element_located((By.XPATH, "//a[@data-marker='pagination-button/nextPage']")))
		button_next = driver.find_element(By.XPATH, "//a[@data-marker='pagination-button/nextPage']")
		button_next.click()
		