from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC


url = 'https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin'
userName = 'ben'
password = '123456'


class ConnectToLinkedin:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def open_browser(self):
        self.driver.get(url)

    def enter_ditales(self):
        element = self.driver.find_element(By.ID, 'username')
        element.click()
        element.send_keys(userName)

        element.find_element(By.ID, 'password')
        element.click()
        element.send_keys(password)

        element.find_element(By.CLASS_NAME, 'btn__primary--large from__button--floating')
        element.click()

