import logging
import traceback
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

from parser import Parser
from service import Service
from utils import Utils

class Runner:
	pars = Parser()
	serv = Service()
	util = Utils()
	
	def run(self):
		options = Options()
		options.add_argument("--headless")
		driver = webdriver.Chrome(options=options)
		wait = WebDriverWait(driver, 20)
		flats_list = []
		self.pars.get_url(driver)
		path = self.util.input_path()
		print(f'Парсинг сайта начался {datetime.now().strftime("%H:%M:%S")} {driver.current_url}')
		while True:
			try:
				flats = self.pars.start_pars(driver)
				flats_list.extend(flats)
				count = driver.current_url[-2:].replace('=', '')
				print(
					f'{count}. Спаршено со страницы: {len(flats)} квартир {datetime.now().strftime("%H:%M:%S")}'
					f' {driver.current_url}'
					)
				if count == '00':
					self.serv.save_to_json(flats_list, path)
					break
				else:
					self.pars.new_page(driver, wait)
			
			except AttributeError:
				print('Подтвердите капчу!!')
			
			
			except (Exception, KeyboardInterrupt):
				traceback.print_exc()
				self.serv.save_to_json(flats_list, path)
				break


if __name__ == '__main__':
	run = Runner()
	logging.basicConfig(level=logging.CRITICAL)
	run.run()