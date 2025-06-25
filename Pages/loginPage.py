from selenium.webdriver.common.by import By

from Locators.locators import Locators


class LoginPage():

    def __init__(self, driver):
        self.driver = driver

        self.username_input_id = Locators.username_input_id
        self.password_input_id = Locators.password_input_id
        self.login_button_id = Locators.login_button_id

    def enter_username(self, username):
        self.driver.find_element(By.ID, self.username_input_id).clear()
        self.driver.find_element(By.ID, self.username_input_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.password_input_id).clear()
        self.driver.find_element(By.ID, self.password_input_id).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.ID, self.login_button_id).click()