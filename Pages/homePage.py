from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Locators.locators import Locators

class HomePage():

    def __init__(self, driver):
        self.driver = driver

        self.username_input_id = Locators.username_input_id
        self.logout_link_id = Locators.logout_link_id
        self.hamburger_menu_id = Locators.hamburger_menu_id

    def click_hamburger(self):
        hamburger_menu = WebDriverWait(self.driver, 300).until(
            EC.presence_of_element_located((By.ID, self.hamburger_menu_id))
        )
        hamburger_menu.click()

    def logout(self):
        logout_link = WebDriverWait(self.driver, 300).until(
            EC.presence_of_element_located((By.ID, self.logout_link_id))
        )
        logout_link.click()