from selenium import webdriver
from selenium.webdriver.common.by.By


class LoginPage(self):

	# Driver constructor
	# can include multiple drivers for cross browser testing 
	def __init__(self, driver):
		self._driver = webdriver.Chrome()
	# self._driver = webdriver.Safari()
	# self._driver = webdriver.Firefox() 


	# find the locator/selector id by using page inspect
	# username_box
	# password_box
	# login_button

	# login method


	def login(self):
		

		username_input = driver.find_element_by_id()


		password_input = driver.find_element_by_id()

	def search(self):

		find_by()