__author__ = 'zhang'

import unittest

class Class2(unittest.TestCase):

    def setUp(self):
        #self.driver = webdriver.Firefox(firefox_profile='D:/ff_profile',executable_path='D:/geckodriver.exe')
        print('tc setup')

    def test_class2_future1(self):
#         driver = self.driver
#         driver.get('https://192.168.2.203')
#         driver.find_elements_by_id('j_username')[0].send_keys('admin')
#         driver.find_elements_by_id('j_password')[0].send_keys('123456')
#         driver.find_element_by_xpath("//span[@noc.key='LOGIN']").click()
#         print (driver.title)
        print('test class2 future1')
    
    def test_class2_future2(self):
        print('test class2 future2')
    
    def tearDown(self):
        print('tc teardown')
        # self.driver.quit()

    @classmethod  
    def setUpClass(cls):  
        print("class2 setUpClass")  
 
    @classmethod  
    def tearDownClass(cls):  
        print()  
        print("class2 tearDownClass")  
        
