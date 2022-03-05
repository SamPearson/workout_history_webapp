#Selenium and webdriver
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

#Selenium selection tools
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# TODO - do not hardcode this URL
test_url = "http://127.0.0.1:5000/"


class TestSmoke:

    driver = ''

    def setup_method(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.implicitly_wait(5) #wait up to 5 seconds for any element
        self.driver.get(test_url)

    def test_smoke(self):

        # Confirm the login title is present
        expected_title_text = 'Log In'
        actual_title_text = self.driver.find_element(By.TAG_NAME, 'h3').text

        assert expected_title_text == actual_title_text, f'Error, expected text {expected_title_text}, but actual text: {actual_title_text}'

    def teardown_method(self):
        self.driver.quit()
