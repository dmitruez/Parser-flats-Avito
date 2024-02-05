from selenium import webdriver
from parser import Parser
from selenium.webdriver.support.ui import WebDriverWait


class Runner:
	pars = Parser()
	
	def run(self):
		driver = webdriver.Chrome()
		wait = WebDriverWait(driver, 10)
		self.pars.get_url(driver)
		flats = self.pars.start_pars(driver)
		self.pars.new_page(driver, wait)
		

run = Runner()
run.run()