import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class TestAmazonBestSellers:
    driver = ''
    def setup(self):
        self.driver = webdriver.Chrome(executable_path='/Users/alilie/Desktop/Selenium_project/chromedriver')
        self.driver.implicitly_wait(5)
        self.driver.get('https://www.amazon.com/')

    def test_best_sellers(self):
        self.driver.find_element(By.XPATH,"//div[@id='nav-xshop']/a[contains(@href, 'gold')]").click()
        #find element va returna o eroare dc nu il gaseste iar find elements nu va returna o eroare dc nu gaseste niste elemente
        # actual_links = self.driver.find_elements(By.XPATH, "//div[@id='nav-xshop']/a")
        # assert len(actual_links) == 5, f"Expected 5 but found {len(actual_links)}"

    def teardown_method(self):
        self.driver.quit()