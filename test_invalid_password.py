import logging, os, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

os.makedirs("logs", exist_ok=True)
os.makedirs("screenshots", exist_ok=True)

logging.basicConfig(filename="logs/test_invalid_password.log", level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s")

service = Service("C:/test-by-me/msedgedriver.exe")
driver = webdriver.Edge(service=service)
driver.get("https://www.saucedemo.com")
logging.info("Opened site for invalid password test")

driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("wrong_password")
driver.find_element(By.ID, "login-button").click()
time.sleep(2)

driver.save_screenshot("screenshots/invalid_password.png")

error_present = driver.find_elements(By.CLASS_NAME, "error-message-container")
if error_present:
    logging.info("✅ Error shown for invalid password")
    print("✅ Invalid password test passed")
else:
    logging.error("❌ No error shown")
    print("❌ Invalid password test failed")
driver.quit()
