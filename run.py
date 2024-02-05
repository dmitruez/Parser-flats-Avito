from selenium import webdriver
from parser import Parser



class Runner:
	pars = Parser()
	
	def run(self):
		driver = webdriver.Chrome()
		self.pars.get_url(driver)