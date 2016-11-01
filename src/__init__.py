__author__ = 'zhang'

import unittest
import login

def setUpModule():  
    print("setUpModule")  
   
def tearDownModule():  
    print("tearDownModule")  

def suit():
    ts = unittest.TestSuite()
    ts.addTest(login('log'))
    ts.addTest(class2())
    unittest.TextTestRunner().run(ts)
    

if __name__ == '__main__':
    suit()