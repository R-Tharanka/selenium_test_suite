# Selenium Test Suite for SauceDemo

This project contains a suite of automated tests for the [SauceDemo](https://www.saucedemo.com) website. The tests are written in Python using the Selenium WebDriver library and are designed to validate various functionalities of the website.

## Project Structure

```
automate_testing/
├── config.py                # Configuration file for test settings
├── test_add_to_cart_ui.py   # Test for adding items to the cart
├── test_invalid_password.py # Test for invalid password login
├── test_long_username.py    # Test for boundary value (long username)
├── test_valid_login.py      # Test for valid login
├── logs/                    # Directory for log files
├── screenshots/             # Directory for screenshots
```

## Prerequisites

- Python 3.8 or higher
- Selenium WebDriver library
- Microsoft Edge browser
- EdgeDriver executable

## Setup Instructions

1. Clone this repository to your local machine.
2. Install the required Python packages:
   ```bash
   pip install selenium
   ```
3. Update the `config.py` file with the correct path to your EdgeDriver executable:
   ```python
   EDGE_DRIVER_PATH = "C:/path/to/your/msedgedriver.exe"
   ```

## Running the Tests

Each test file is standalone and can be executed individually. Use the following command to run a test:

```bash
python test_valid_login.py
```

Replace `test_valid_login.py` with the name of the test file you want to run.

## Test Descriptions

### 1. `test_valid_login.py`
- Verifies that a user can log in with valid credentials.
- Takes a screenshot of the inventory page upon successful login.

### 2. `test_invalid_password.py`
- Verifies that an error message is displayed when logging in with an invalid password.
- Takes a screenshot of the error message.

### 3. `test_long_username.py`
- Tests the boundary value by entering an extremely long username.
- Verifies that an error message is displayed.
- Takes a screenshot of the error message.

### 4. `test_add_to_cart_ui.py`
- Verifies that an item can be added to the cart.
- Checks that the cart badge updates correctly.
- Takes a screenshot of the cart page.

## Logs and Screenshots

- Logs are saved in the `logs/` directory with detailed information about each test run.
- Screenshots are saved in the `screenshots/` directory for visual validation of test results.

## Notes

- Ensure that the EdgeDriver version matches your Microsoft Edge browser version.
- The tests are configured to run on the SauceDemo website and may require updates if the website changes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
