# Improved readability by organizing imports and adding comments for clarity

# Import necessary modules
import logging
import os
import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from datetime import datetime
from config import EDGE_DRIVER_PATH

# Setup folders for logs and screenshots
os.makedirs("logs", exist_ok=True)
os.makedirs("screenshots", exist_ok=True)

# Configure logging
logging.basicConfig(
    filename="logs/test_long_username.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Initialize EdgeDriver
service = Service(EDGE_DRIVER_PATH)
driver = webdriver.Edge(service=service)

try:
    logging.info("Test Case 4: Boundary Value Test – Long Username")

    # Navigate to the site
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    time.sleep(1)

    # Input extremely long username
    long_username = "user_" + "x" * 100
    driver.find_element(By.ID, "user-name").send_keys(long_username)
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)

    # Check for error message
    error_elements = driver.find_elements(By.CLASS_NAME, "error-message-container")
    if error_elements:
        logging.info("✅ Login failed as expected with long username.")
        print("✅ Boundary test passed")
    else:
        logging.warning("❌ Login did not show error – possible input validation issue.")
        print("❌ Boundary test failed")

    # Take a screenshot
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    screenshot_path = f"screenshots/long_username_{timestamp}.png"
    driver.save_screenshot(screenshot_path)
    logging.info(f"Screenshot saved at {screenshot_path}")

except Exception as e:
    logging.error(f"Test failed with error: {str(e)}")
    print("❌ Test encountered an error")

finally:
    # Quit the driver
    driver.quit()
    logging.info("Test execution completed.")
