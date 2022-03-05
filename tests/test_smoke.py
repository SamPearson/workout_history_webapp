#Selenium and webdriver
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

#Selenium selection tools
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# TODO - do not hardcode this data
test_url = "http://127.0.0.1:5000/"
test_email = "bozo@gmail.com"
test_password = "1234567"


class TestSmoke:

    driver = ''

    def setup_method(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.implicitly_wait(5) #wait up to 5 seconds for any element
        self.driver.get(test_url)

    def test_login_redirect(self):
        expected_title_text = 'Log In'
        actual_title_text = self.driver.find_element(By.ID, 'titlebar').text

        assert expected_title_text == actual_title_text, f'Error, expected text {expected_title_text}, but actual text: {actual_title_text}'

    def login(self):
        self.driver.get(f'{test_url}/login')
        self.driver.find_element(By.ID, 'email').send_keys(test_email)
        self.driver.find_element(By.ID, 'password').send_keys(test_password, Keys.ENTER)

    def test_login(self):
        self.login()

        expected_alert_text = 'Logged in successfully!'
        actual_alert_text = self.driver.find_element(By.CLASS_NAME, 'alert').text

        # TODO - alert div contains extra characters; it can't be compared directly to the expected text
        assert expected_alert_text in actual_alert_text, f'Error, expected text {expected_alert_text}, but actual text: {actual_alert_text}'

    def test_logout(self):
        self.login()

        self.driver.find_element(By.ID, 'logout').click()

        expected_title_text = 'Log In'
        actual_title_text = self.driver.find_element(By.ID, 'titlebar').text
        assert expected_title_text == actual_title_text, f'Error, expected text {expected_title_text}, but actual text: {actual_title_text}'



    def teardown_method(self):
        self.driver.quit()
