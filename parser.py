from bs4 import BeautifulSoup as Bs
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
import time
from entity import Flat


class Parser:
	URL = ("https://www.avito.ru/sankt-peterburg/kvartiry/sdam/na_dlitelnyy_srok-ASgBAgICAkSSA8gQ8AeQUg?context"
	       "=H4sIAAAAAAAA_0q0MrSqLraysFJKK8rPDUhMT1WyLrYyNLNSKk5NLErOcMsvyg3PTElPLVGyrgUEAAD__xf8iH4tAAAA&p=98")
	
	
	def get_url(self, driver: webdriver.Chrome):
		driver.get(self.URL)
	
	
	@staticmethod
	def start_pars(driver: webdriver.Chrome):
		WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.TAG_NAME, "html")))
		html = driver.page_source
		soup = Bs(html, 'lxml')
		flats = []
		blok = soup.find('div', class_="items-items-kAJAg")
		elements = blok.select('.items-items-kAJAg > div')
		time.sleep(0.2)
		div_flats = list(map(lambda m: m if len(m.text) > 1 else elements.pop(elements.index(m)), elements))
		for flat in div_flats:
			try:
				price = flat.find('meta', attrs={"itemprop": "price"})["content"]
				
				area_list = flat.find('div', class_='iva-item-title-py3i_').text.split(", ")
				if len(area_list) == 3:
					area = area_list[1].split()[0].replace(',', '.')
				else:
					area = area_list[1] + area_list[2].split()[0]
				
				description = flat.find(
					'div', class_="iva-item-descriptionStep-C0ty1"
					).text.replace(
					'\n',
					' '
					).replace(
					' ', ' '
					)
				
				div_href = flat.find('a')['href']
				href = 'https://www.avito.ru' + div_href
				a = Flat(
					price=float(price),
					area=float(area),
					description=str(description),
					href=str(href)
					)
				flats.append(a)
			except TypeError:
				pass
		return flats
	
	
	def new_page(self, driver: webdriver.Chrome, wait: WebDriverWait):
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight - 1700);")
		try:
			wait.until(
				ec.visibility_of_element_located((By.CSS_SELECTOR, ".styles-module-item_size_s-Tvz95"))
				)
			
			button_next = driver.find_elements(By.CSS_SELECTOR, ".styles-module-item_size_s-Tvz95")[8]
			button_next.click()
		
		except Exception as e:
			driver.refresh()
			driver.execute_script("window.scrollTo(0, document.body.scrollHeight - 1700);")
			self.new_page(driver, wait)