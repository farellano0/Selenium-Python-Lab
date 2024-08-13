import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

class base_test(unittest.TestCase):

    def setUp(self):
        self.service = Service("C:\\Drivers\\chromedriver.exe")
        self.driver = webdriver.Chrome(service = self.service)
        self.driver.implicitly_wait(15)

    def test1(self):
        driver = self.driver
        driver.get("https://demoqa.com/")
        time.sleep(5)

    def tearDown(self):
        driver = self.driver
        driver.quit()
        
if __name__ == "__main__":
    unittest.main()