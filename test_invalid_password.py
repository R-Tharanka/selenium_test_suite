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
os.makedirs("logs", exist_ok=True)
os.makedirs("screenshots", exist_ok=True)

# Configure logging
logging.basicConfig(
    filename="logs/test_invalid_password.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Initialize EdgeDriver
service = Service(EDGE_DRIVER_PATH)
driver = webdriver.Edge(service=service)

try:
    # Open the SauceDemo site
    driver.get("https://www.saucedemo.com")
    logging.info("Opened site for invalid password test")

    # Attempt login with invalid password
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("wrong_password")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)

    # Take a screenshot
    driver.save_screenshot("screenshots/invalid_password.png")

    # Check for error message
    error_present = driver.find_elements(By.CLASS_NAME, "error-message-container")
    if error_present:
        logging.info("✅ Error shown for invalid password")
        print("✅ Invalid password test passed")
    else:
        logging.error("❌ No error shown")
        print("❌ Invalid password test failed")

finally:
    # Quit the driver
    driver.quit()
