import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

class PruebaLogin(unittest.TestCase):

    def setUp(self):
        self.service = Service("C:\\Drivers\\chromedriver.exe")
        self.driver = webdriver.Chrome(service = self.service)
        self.driver.implicitly_wait(15)
        self.t = 3

    def test_login1(self):
        driver = self.driver
        t = self.t
        
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        time.sleep(t)
        
        username = driver.find_element(By.XPATH, "//input[@id='user-name']")
        password = driver.find_element(By.XPATH, "//input[@id='password']")
        btn = driver.find_element(By.XPATH, "//input[@id='login-button']")
        
        username.send_keys("Fernando")
        password.send_keys("admin123")
        btn.click()
        
        error = driver.find_element(By.XPATH, "//h3[@data-test='error']")
        error = error.text
        #print(error)
        if(error == "Epic sadface: Username and password do not match any user in this service"):
            print("El error de los datos es correcto")
            print("Prueba uno OK")
        time.sleep(t)

    def test_login2(self):
            driver = self.driver
            t = self.t
            
            driver.get("https://www.saucedemo.com/")
            driver.maximize_window()
            time.sleep(t)
            
            username = driver.find_element(By.XPATH, "//input[@id='user-name']")
            password = driver.find_element(By.XPATH, "//input[@id='password']")
            btn = driver.find_element(By.XPATH, "//input[@id='login-button']")
            
            password.send_keys("admin123")
            btn.click()
            
            error = driver.find_element(By.XPATH, "//h3[@data-test='error']")
            error = error.text
            # print(error)
            if(error == "Epic sadface: Username is required"):
                print("Falta el username")
                print("Prueba dos OK")
            time.sleep(t)
            
    def test_login3(self):
            driver = self.driver
            t = self.t
            
            driver.get("https://www.saucedemo.com/")
            driver.maximize_window()
            time.sleep(t)
            
            username = driver.find_element(By.XPATH, "//input[@id='user-name']")
            password = driver.find_element(By.XPATH, "//input[@id='password']")
            btn = driver.find_element(By.XPATH, "//input[@id='login-button']")
            
            username.send_keys("Fernando")
            btn.click()
            
            error = driver.find_element(By.XPATH, "//h3[@data-test='error']")
            error = error.text
            print(error)
            if(error == "Epic sadface: Password is required"):
                print("Falta el password")
                print("Prueba tres OK")
            time.sleep(t)
            
    def test_login4(self):
            driver = self.driver
            t = self.t
            
            driver.get("https://www.saucedemo.com/")
            driver.maximize_window()
            time.sleep(t)
            
            username = driver.find_element(By.XPATH, "//input[@id='user-name']")
            password = driver.find_element(By.XPATH, "//input[@id='password']")
            btn = driver.find_element(By.XPATH, "//input[@id='login-button']")
            
            btn.click()
            
            error = driver.find_element(By.XPATH, "//h3[@data-test='error']")
            error = error.text
            print(error)
            if(error == "Epic sadface: Username is required"):
                print("Faltan ambos campos")
                print("Prueba cuatro OK")
            time.sleep(t)
            
    def test_login4(self):
            driver = self.driver
            t = self.t
            
            driver.get("https://www.saucedemo.com/")
            driver.maximize_window()
            time.sleep(t)
            
            username = driver.find_element(By.XPATH, "//input[@id='user-name']")
            password = driver.find_element(By.XPATH, "//input[@id='password']")
            btn = driver.find_element(By.XPATH, "//input[@id='login-button']")
            
            username.send_keys("standard_user")
            password.send_keys("secret_sauce")
            btn.click()
            
            try:
                logo = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='app_logo'][contains(.,'Swag Labs')]")))
                print(logo.is_displayed())
            except TimeoutException as ex:
                print(ex.msg)
                print("No cargo la página al iniciar sesión")
                
            time.sleep(t)


    def tearDown(self):
        driver = self.driver
        driver.quit()
        
if __name__ == "__main__":
    unittest.main()