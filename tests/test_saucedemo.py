# pyrefly: ignore [missing-import]
from selenium import webdriver
# pyrefly: ignore [missing-import]
from selenium.webdriver.common.by import By
# pyrefly: ignore [missing-import]
from selenium.webdriver.chrome.service import Service
# pyrefly: ignore [missing-import]
from webdriver_manager.chrome import ChromeDriverManager
# pyrefly: ignore [missing-import]
import pytest
import time

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    })
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument("--disable-features=PasswordLeakDetection")
    # Đã tắt headless để trình duyệt hiển thị lên màn hình cho sinh viên xem
    options.add_argument('--window-size=1920,1080')
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_login_and_sort(driver):
    driver.get("https://www.saucedemo.com/")
    time.sleep(1)
    
    username_input = driver.find_element(By.ID, "user-name")
    username_input.send_keys("standard_user")
    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys("secret_sauce")
    time.sleep(1)
    
    driver.find_element(By.ID, "login-button").click()
    time.sleep(1)
    
    filter_dropdown = driver.find_element(By.CLASS_NAME, "product_sort_container")
    filter_dropdown.click()
    time.sleep(1)
    
    driver.find_element(By.XPATH, "//option[@value='za']").click()
    time.sleep(1)
    
    assert "inventory.html" in driver.current_url

def test_add_to_cart_and_checkout_step_1(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(1)
    
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    time.sleep(1)
    
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    time.sleep(1)
    
    driver.find_element(By.ID, "checkout").click()
    time.sleep(1)
    
    driver.find_element(By.ID, "first-name").send_keys("John")
    driver.find_element(By.ID, "last-name").send_keys("Doe")
    driver.find_element(By.ID, "postal-code").send_keys("12345")
    time.sleep(1)
    
    assert "checkout-step-one.html" in driver.current_url

def test_checkout_complete_and_logout(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    driver.find_element(By.ID, "checkout").click()
    driver.find_element(By.ID, "first-name").send_keys("John")
    driver.find_element(By.ID, "last-name").send_keys("Doe")
    driver.find_element(By.ID, "postal-code").send_keys("12345")
    driver.find_element(By.ID, "continue").click()
    time.sleep(1)
    
    driver.find_element(By.ID, "finish").click()
    time.sleep(1)
    
    driver.find_element(By.ID, "back-to-products").click()
    time.sleep(1)
    
    driver.find_element(By.ID, "react-burger-menu-btn").click()
    time.sleep(1)
    
    driver.find_element(By.ID, "logout_sidebar_link").click()
    time.sleep(1)
    
    assert "saucedemo.com" in driver.current_url

if __name__ == "__main__":
    pytest.main(["-v", "-s", __file__])
