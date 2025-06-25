from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import time
import unittest

from Locators.locators import Locators
from Pages.loginPage import LoginPage
from Pages.homePage import HomePage
import HtmlTestRunner





BASE_URL = "https://www.saucedemo.com/"
INVENTORY_URL = "https://www.saucedemo.com/inventory.html"
ACTUAL_ERROR_MESSAGE = "Epic sadface: Username and password do not match any user in this service"
THANK_YOU_MESSAGE = '''Thank you for your order!
Your order has been dispatched, and will arrive just as fast as the pony can get there!
Back Home'''

class LoginTest(unittest.TestCase):  # Fixed typo: LoginTet -> LoginTest

    @classmethod
    def setUpClass(cls):
        # Configure Chrome options to disable password manager
        chrome_options = Options()
        chrome_options.add_experimental_option("prefs", {
            "profile.password_manager_leak_detection": False,
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False  # Added this line
        })
        
        # Initialize Chrome driver with options
        cls.driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=chrome_options
        )
        cls.driver.get(BASE_URL)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_not_valid(self):
        driver = self.driver
        login = LoginPage(driver)
        login.enter_username('wrongName')
        login.enter_password('wrongPassword')
        login.click_login()
        actual_text = WebDriverWait(self.driver, 100).until(
            EC.presence_of_element_located((By.XPATH, Locators.alert_message_xpath))
        ).text
        self.assertIn(ACTUAL_ERROR_MESSAGE, 
                      actual_text, 
                      f'Login failed with message: {actual_text} instead of showing {ACTUAL_ERROR_MESSAGE}')

    def test_login_valid(self):
        driver = self.driver
        login = LoginPage(driver)
        login.enter_username('standard_user')
        login.enter_password('secret_sauce')
        login.click_login()

        WebDriverWait(self.driver, 5).until(EC.url_to_be(INVENTORY_URL))
        self.assertEqual(self.driver.current_url, INVENTORY_URL)

        """Method 1: Find all 'Add to cart' buttons and click them"""
        try:
            # Find all "Add to cart" buttons
            add_to_cart_buttons = self.driver.find_elements(By.CLASS_NAME, Locators.price_bar_class_name)
            
            print(f"Found {len(add_to_cart_buttons)} 'Add to cart' buttons")
            
            # Click each button
            for i, button in enumerate(add_to_cart_buttons):
                try:
                    # Scroll to button to ensure it's visible
                    self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
                    
                    # Use WebDriverWait instead of time.sleep
                    WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(button))
                    
                    button.click()
                    print(f"Clicked 'Add to cart' button {i+1}")
                    
                    # Wait for badge to update
                    WebDriverWait(self.driver, 5).until(
                        EC.text_to_be_present_in_element((By.CLASS_NAME, Locators.shopping_cart_badge_class_name), str(i+1))
                    )
                    
                    badge_text = self.driver.find_element(By.CLASS_NAME, Locators.shopping_cart_badge_class_name).text
                    self.assertEqual(str(i+1), badge_text, 
                                   f"After adding item {i+1}, badge should show {i+1}, but shows {badge_text}")
                    
                except Exception as e:
                    print(f"Error clicking button {i+1}: {e}")

        except Exception as e:
            print(f"Error finding add to cart buttons: {e}")
            
        
        """Method 2: Go to cart and checkout all items"""
        
        # Find "shopping_cart_link" button
        shopping_cart_link_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, Locators.shopping_cart_link_class_name))
        )

        # Scroll to button to ensure it's visible
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", shopping_cart_link_button)
        shopping_cart_link_button.click()

        # Find "checkout" button and click
        checkout_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, Locators.checkout_button_id))
        )

        # Scroll to button to ensure it's visible
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", checkout_button)
        checkout_button.click()

        # Fill personal information
        first_name_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, Locators.first_name_input_id))
        )
        first_name_input.send_keys("DUMNE")

        last_name_input = self.driver.find_element(By.ID, Locators.last_name_input_id)
        last_name_input.send_keys("VIJAY")

        postal_code_input = self.driver.find_element(By.ID, Locators.postal_code_input_id)
        postal_code_input.send_keys("500001")

        # Click continue
        continue_button = self.driver.find_element(By.ID, Locators.continue_button_id)
        continue_button.click()

        # Click finish
        finish_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, Locators.finish_button_id))
        )

        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", finish_button)
        finish_button.click()

        # Wait for thank you message element is displayed, then get text
        thank_you_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, Locators.checkout_complete_container_id))
        )
        thank_you_text = thank_you_element.text
        self.assertEqual(THANK_YOU_MESSAGE, thank_you_text)

        # Go back home
        back_home_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, Locators.back_home_button_id))
        )
        back_home_button.click()

        # Logout
        homePage = HomePage(self.driver)
        homePage.click_hamburger()
        homePage.logout()
        
        print("Logout successful")
            


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit() 
        print("Test Completed")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))

