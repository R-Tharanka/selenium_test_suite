import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
import time
import os
from config import EDGE_DRIVER_PATH

# Setup logging
log_dir = "logs"
screenshot_dir = "screenshots"
os.makedirs(log_dir, exist_ok=True)
os.makedirs(screenshot_dir, exist_ok=True)

logging.basicConfig(
    filename=os.path.join(log_dir, "test_valid_login.log"),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Launch browser
service = Service(EDGE_DRIVER_PATH)
driver = webdriver.Edge(service=service)
driver.get("https://www.saucedemo.com")
logging.info("Opened SauceDemo site")

# Fill login form
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
logging.info("Submitted login form with valid credentials")

# Wait and validate
time.sleep(2)
screenshot_path = os.path.join(screenshot_dir, "valid_login.png")
driver.save_screenshot(screenshot_path)

if "inventory" in driver.current_url:
    logging.info("✅ Test Passed: Reached inventory page")
    print("✅ Test Passed: Valid login successful.")
else:
    logging.error("❌ Test Failed: Did not reach inventory page")
    print("❌ Test Failed: Valid login did not reach inventory page.")

driver.quit()
