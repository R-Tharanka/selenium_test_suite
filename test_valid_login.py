# Improved readability by organizing imports and adding comments for clarity

# Import necessary modules
import logging
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from config import EDGE_DRIVER_PATH

# Setup folders for logs and screenshots
log_dir = "logs"
screenshot_dir = "screenshots"
os.makedirs(log_dir, exist_ok=True)
os.makedirs(screenshot_dir, exist_ok=True)

# Configure logging
logging.basicConfig(
    filename=os.path.join(log_dir, "test_valid_login.log"),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Initialize EdgeDriver
service = Service(EDGE_DRIVER_PATH)
driver = webdriver.Edge(service=service)

try:
    # Open the SauceDemo site
    driver.get("https://www.saucedemo.com")
    logging.info("Opened SauceDemo site")

    # Fill login form with valid credentials
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

finally:
    # Quit the driver
    driver.quit()
