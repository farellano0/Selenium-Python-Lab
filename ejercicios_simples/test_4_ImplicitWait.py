from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

PATH = "C:\\Drivers\\chromedriver.exe"
s = Service(PATH)
driver = webdriver.Chrome(service = s)
t = 1

driver.get("https://demoqa.com/text-box")
driver.maximize_window()
driver.implicitly_wait(15)

nom = driver.find_element(By.XPATH, "//input[@id='userName']")
email = driver.find_element(By.XPATH, "//input[@id='userEmail']")
currentAddress = driver.find_element(By.XPATH, "//textarea[@id='currentAddress']")
permantAddress = driver.find_element(By.XPATH, "//textarea[@id='permanentAddress']")
btnSubmit = driver.find_element(By.XPATH, "//button[@id='submit']")


nom.send_keys("Fernando")
time.sleep(t)

email.send_keys("farellano0@gmail.com")
time.sleep(t)

currentAddress.send_keys("Dirección uno.")
time.sleep(t)

permantAddress.send_keys("Dirección dos")
time.sleep(t)

driver.execute_script("window.scrollTo(0,500)")
time.sleep(t)

btnSubmit.click()
time.sleep(t)

displayNom= driver.find_element(By.XPATH, "//p[contains(.,'Fernando')]")
displayEmail= driver.find_element(By.XPATH, "//p[contains(.,'farellano0@gmail.com')]")
displayCurrentAddress= driver.find_element(By.XPATH, "//p[contains(.,'Dirección uno')]")
displayPermantAddress= driver.find_element(By.XPATH, "//p[contains(.,'Dirección dos')]")

print(displayNom.is_displayed())    
print(displayEmail.is_displayed())    
print(displayCurrentAddress.is_displayed())    
print(displayPermantAddress.is_displayed())    

driver.close()