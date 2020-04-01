#from django. import SeleniumTestCase
from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase


class SeleniumTests(StaticLiveServerTestCase):
    def setUp(cls):
        cls.selenium = webdriver.Chrome(executable_path = '/home/maria/Projects/2020-1-Track-Backend-M-Kerechanina/messenger_app/geckodriver')
        cls.selenium.get('http://127.0.0.1:8000/chats/send_message_with_html/')
        cls.selenium.implicitly_wait(10)

    def test_send_msg(self):
        message_input = self.driver.find_element_by_id('id_content')
        message_input.send_keys('my_message')
        assert message_input is not None

        elem = self.driver.find_element_by_class_name()
        elem.click()
        assert elem is not None