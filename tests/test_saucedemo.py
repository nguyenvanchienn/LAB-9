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
# pyrefly: ignore [missing-import]
import time

@pytest.fixture
def driver():
    # Khởi tạo browser với webdriver_manager để tránh lỗi Selenium Manager trên Python 3.14
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless') # Bỏ comment nếu muốn chạy ngầm
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    # Đóng browser sau khi test xong
    driver.quit()

def test_valid_login(driver):
    driver.get("https://www.saucedemo.com/")
    
    # Nhập username
    username_input = driver.find_element(By.ID, "user-name")
    username_input.send_keys("standard_user")
    
    # Nhập password
    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys("secret_sauce")
    
    # Click login
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()
    
    # Kiểm tra xem đã đăng nhập thành công và chuyển đến trang inventory chưa
    assert "inventory.html" in driver.current_url
    
    # Kiểm tra tiêu đề trang
    title = driver.find_element(By.CLASS_NAME, "title").text
    assert title == "Products"

def test_invalid_login(driver):
    driver.get("https://www.saucedemo.com/")
    
    # Nhập username sai
    username_input = driver.find_element(By.ID, "user-name")
    username_input.send_keys("locked_out_user")
    
    # Nhập password
    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys("secret_sauce")
    
    # Click login
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()
    
    # Kiểm tra thông báo lỗi
    error_message = driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
    assert "Epic sadface: Sorry, this user has been locked out." in error_message

def test_add_to_cart(driver):
    driver.get("https://www.saucedemo.com/")
    
    # Login trước
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    
    # Thêm sản phẩm đầu tiên vào giỏ hàng
    add_to_cart_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
    add_to_cart_button.click()
    
    # Kiểm tra số lượng item trong giỏ hàng tăng lên 1
    cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert cart_badge == "1"
    
    # Vào giỏ hàng kiểm tra tên sản phẩm
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    item_name = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    assert item_name == "Sauce Labs Backpack"
