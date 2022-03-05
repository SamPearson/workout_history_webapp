#Selenium and webdriver
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

#Selenium selection tools
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#todo - get environment name and url from file
test_url = "http://127.0.0.1:5000/"

def test_smoke():
    #Launch browser

    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    driver.implicitly_wait(5) #wait up to 5 seconds for any element
    driver.get(test_url)

    #Confirm the login title is present
    expected_title_text = 'Log In'
    actual_title_text = driver.find_element(By.TAG_NAME, 'h3').text

    assert expected_title_text == actual_title_text, f'Error, expected text {expected_title_text}, but actual text: {actual_title_text}'
    driver.quit()
