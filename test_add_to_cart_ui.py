import logging, os, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from config import EDGE_DRIVER_PATH

# Setup folders
os.makedirs("logs", exist_ok=True)
os.makedirs("screenshots", exist_ok=True)

logging.basicConfig(filename="logs/test_add_to_cart_ui.log", level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s")

# Start Edge
service = Service(EDGE_DRIVER_PATH)
driver = webdriver.Edge(service=service)
driver.get("https://www.saucedemo.com")
logging.info("Opened SauceDemo site for Add to Cart UI test")

# Login
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
time.sleep(2)

# Add item to cart
add_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
add_button.click()
logging.info("Clicked on 'Add to Cart' for Sauce Labs Backpack")

# Validate cart icon shows "1"
cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
screenshot_path = "screenshots/add_to_cart_ui.png"
driver.save_screenshot(screenshot_path)

if cart_badge.text == "1":
    logging.info("✅ Cart badge updated correctly to 1")
    print("✅ Add to Cart UI test passed")
else:
    logging.error("❌ Cart badge did not update correctly")
    print("❌ Add to Cart UI test failed")

driver.quit()
