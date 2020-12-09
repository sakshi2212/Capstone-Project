from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from django.urls import reverse
import time


class AccountTestCase(LiveServerTestCase):

    def setUp(self):
        self.selenium = webdriver.Chrome(r'C:\Users\SAKSHI\.wdm\drivers\chromedriver\win32\86.0.4240.22\chromedriver.exe')

    def tearDown(self):
        self.selenium.quit()

    def test_register(self):
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}
        selenium = self.selenium

        selenium.get(self.live_server_url+reverse('register'))
        url=self.live_server_url

        selenium.find_element_by_name('first_name').send_keys('Sakshi')
        selenium.find_element_by_name('last_name').send_keys('')
        selenium.find_element_by_name('username')
        selenium.find_element_by_name('password')

        selenium.find_element_by_name('submit').click()
        time.sleep(10)
        self.assertEquals(self.live_server_url,url)


    def test_login(self):
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}
        selenium = self.selenium
        selenium.get(self.live_server_url)
        url=self.live_server_url+reverse('app')
        username = selenium.find_element_by_name('username')
        password = selenium.find_element_by_name('password')

        submit = selenium.find_element_by_name('submit')

        username.send_keys('bt17gcs001')
        password.send_keys('admin')

        submit.click()
        time.sleep(10)
        self.assertEquals(self.live_server_url,url)

