from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestWebsitetHomePageChrome(TestCase):

    def setUp(self):
        self.base_url = 'http://web:8000'
        self.chrome = webdriver.Remote(
            command_executor='http://selenium_hub:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME
        )
   
        self.chrome.implicitly_wait(10)
    def tearDown(self):
        self.chrome.quit()

    def test_home_page_with_chrome(self):
        self.chrome.get('http://web:8000')
        self.assertIn(
            self.chrome.title,
            'List of Events'
        )
    
    def test_login_button_home_page(self):
        self.chrome.get('http://web:8000')
        login_li = self.chrome.find_element_by_id('home-login')
        login_li.find_element_by_tag_name('a').click()
        self.login_url = self.base_url + '/authentication/login/'
        self.assertEquals(
            self.chrome.current_url,
            self.login_url
        )

    def test_register_button_home_page(self):
        self.chrome.get('http://web:8000')
        register_li = self.chrome.find_element_by_id('home-register')
        register_li.find_element_by_tag_name('a').click()
        self.register_url = self.base_url + '/authentication/register/'
        self.assertEquals(
            self.chrome.current_url,
            self.register_url
        )         

class TestWebsitetHomePageFirefox(TestCase):

    def setUp(self):
        self.base_url = 'http://web:8000'
        self.firefox = webdriver.Remote(
            command_executor='http://selenium_hub:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.FIREFOX
        )
        self.firefox.implicitly_wait(10)
        
    def tearDown(self):
        self.firefox.quit()
    
    def test_visit_site_with_firefox(self):
        self.firefox.get('http://web:8000')
        self.assertIn(
            self.firefox.title,
            'List of Events'
        )

    def test_login_button_home_page(self):
        self.firefox.get('http://web:8000')
        login_li = self.firefox.find_element_by_id('home-login')
        login_li.find_element_by_tag_name('a').click()
        self.login_url = self.base_url + '/authentication/login/'
        self.assertEquals(
            self.firefox.current_url,
            self.login_url
        )
    
    def test_register_button_home_page(self):
        self.firefox.get('http://web:8000')
        register_li = self.firefox.find_element_by_id('home-register')
        register_li.find_element_by_tag_name('a').click()
        self.register_url = self.base_url + '/authentication/register/'
        self.assertEquals(
            self.firefox.current_url,
            self.register_url
        )

    