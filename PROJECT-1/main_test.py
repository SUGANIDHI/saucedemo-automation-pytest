import os
import time
import pytest
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Load test data
df = pd.read_excel("buyers.xlsx")

# Create screenshots dir
os.makedirs("screenshots", exist_ok=True)

def login(driver, username, password):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()
    time.sleep(1)
    return "inventory" in driver.current_url

def buy_product(driver, username):
    try:
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        driver.find_element(By.ID, "checkout").click()
        driver.find_element(By.ID, "first-name").send_keys("Test")
        driver.find_element(By.ID, "last-name").send_keys("User")
        driver.find_element(By.ID, "postal-code").send_keys("12345")
        driver.find_element(By.ID, "continue").click()
        driver.find_element(By.ID, "finish").click()
        print(f"✅ Purchase completed for {username}")
    except Exception as e:
        print(f"❌ Could not complete purchase for {username}: {e}")
    finally:
        path = f"screenshots/{username}_screenshot.png"
        driver.save_screenshot(path)
        print(f"📸 Screenshot saved: {path}")

@pytest.mark.parametrize("username,password", df.values)
def test_user_flow(username, password):
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(), options=options)

    try:
        login_success = login(driver, username, password)

        if username == "locked_out_user":
            assert not login_success, f"{username} should NOT be able to login"
            return

        assert login_success, f"Login failed for {username}"

        if username in df["username"].values:
            buy_product(driver, username)

    finally:
        driver.quit()


