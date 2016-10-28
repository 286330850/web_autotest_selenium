__author__ = 'noc'

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Login(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(firefox_profile='D:/ff_profile',executable_path='D:/geckodriver.exe')

    def test_login(self):
        driver = self.driver
        driver.get('https://192.168.2.203')
        driver.find_elements_by_id('j_username')[0].send_keys('admin')
        driver.find_elements_by_id('j_password')[0].send_keys('123456')
        driver.find_element_by_xpath("//span[@noc.key='LOGIN']").click()
        print (driver.title)

    def tearDown(self):
        pass
        # self.driver.quit()

if __name__ == '__main__':
    unittest.main()