#from django. import SeleniumTestCase
from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase


class SeleniumTests(StaticLiveServerTestCase):

    def test_send_msg(self):
        self.selenium = webdriver.Chrome(executable_path = '/home/maria/Projects/2020-1-Track-Backend-M-Kerechanina/chromedriver')
        self.selenium.get('http://127.0.0.1:8000/chats/send_message_with_html/')
        self.selenium.implicitly_wait(10)

        message_input = self.selenium.find_element_by_id('id_content')
        message_input.send_keys('my_message')
        assert message_input is not None

        message_input = self.selenium.find_element_by_id('id_chat')
        message_input.send_keys('chat object (1)')
        assert message_input is not None

        message_input = self.selenium.find_element_by_id('id_user')
        message_input.send_keys('root')
        assert message_input is not None

        elem = self.selenium.find_element_by_tag_name('button')
        elem.click()
        assert elem is not None

        self.selenium.close()