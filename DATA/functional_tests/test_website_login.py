from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class AccountTestCaseChrome(LiveServerTestCase):
    def setUp(self):
        self.base_url = 'http://web:8000'
        self.login_url = 'http://web:8000/authentication/login/'
        self.chrome = webdriver.Remote(
            command_executor='http://selenium_hub:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME
        )
        self.chrome.implicitly_wait(10)

    def tearDown(self):
        self.chrome.quit()

        def test_login(self):
            self.chrome.get(self.login_url)
            username = self.chrome.find_element_by_id('id_username')
            password = self.chrome.find_element_by_id('id_password')
            submit = self.chrome.find_element_by_tag_name('button')
            username.send_keys('test_user')
            password.send_keys('test_password')
            submit.send_keys(Keys.RETURN)