import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class TestAmazon:
    search_words = ('dress', 'shoes', 'toys')

    driver = ''
    def setup(self):
        self.driver = webdriver.Chrome(executable_path='/Users/alilie/Desktop/Selenium_project/chromedriver')
        self.driver.implicitly_wait(5)
        self.driver.get('https://www.amazon.com/') 


    @pytest.mark.parametrize('search_query', search_words)
    def test_amazon(self, search_query):

        # vrem sa interactionam cu bara de search
        search = self.driver.find_element(By.ID, 'twotabsearchtextbox')
        search.send_keys(search_query, Keys.ENTER)  # tastez in casuta

        # verificam ca am cautat dupa dress

        expected_text = f'\"{search_query}\"'
        actual_test = self.driver.find_element(By.XPATH, "//span [@class='a-color-state a-text-bold']").text

        assert expected_text == actual_test, "nu a fost cautat dress cu succes"

    def teardown_method(self):
        self.driver.quit()

