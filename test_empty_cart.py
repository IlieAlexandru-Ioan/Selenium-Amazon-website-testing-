import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class TestAmazonCart:
    driver = ''
    def setup(self):
        self.driver = webdriver.Chrome(executable_path='/Users/alilie/Desktop/Selenium_project/chromedriver')
        self.driver.implicitly_wait(5)
        self.driver.get('https://www.amazon.com/')

    def test_empty_cart(self):
        cart = self.driver.find_element(By.ID, 'nav-cart')
        cart.click()
        actual_text = self.driver.find_element(By.XPATH, "//div[@id='sc-active-cart']//h2").text
        expected_text = "Your Amazon Cart is empty"
        assert expected_text == actual_text, f"error, expected text: {expected_text}, but the actual text: {actual_text}"

    def teardown_method(self):
        self.driver.quit()