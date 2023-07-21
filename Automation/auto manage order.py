from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import re
import time
import csv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Khởi tạo trình duyệt Selenium (ở đây sử dụng Chrome)
driver_path = "/usr/local/bin/"
driver = webdriver.Chrome(driver_path)

# Truy cập vào trang WooCommerce
driver.get("https://famipet.top/wp-admin/edit.php?post_type=shop_order")

# Đăng nhập vào tài khoản quản trị WooCommerce
username = driver.find_element(By.ID, "user_login")
password = driver.find_element(By.ID, "user_pass")
username.send_keys("famipet")
password.send_keys("famipet")
driver.find_element(By.ID, "wp-submit").click()
driver.find_element(By.CSS_SELECTOR, ".wc-processing").click()
time.sleep(5)

list_orders_link = []
list_orders = driver.find_elements(By.CSS_SELECTOR, ".iedit")
for list_order in list_orders:
    order_view = list_order.find_element(By.CSS_SELECTOR, ".order-view")
    order_number = order_view.text
    print(f"Số đơn hàng: {order_number}")
    order_status = list_order.find_element(By.CSS_SELECTOR, ".order-status.status-processing.tips").text
    print(f"Tình trạng đơn hàng: {order_status}")
    outer_html = order_view.get_attribute("href")
    list_orders_link.append(outer_html)
for order_link in list_orders_link:
    driver.get(order_link)
    try:
        order_code = driver.find_element(By.CSS_SELECTOR, ".button.button-link-delete.ghn_cancel_order")
        print(f"Đã có mã vận đơn.")
    except:
        create_bill = driver.find_element(By.CSS_SELECTOR, ".button.button-primary.ghn_creat_order_popup")
        click_bill = create_bill.click()
        create_order = driver.find_element(By.CSS_SELECTOR, ".button.button-primary.devvn_float_right.devvn_ghn_creat_order")
        click_create = create_order.click()
        print(f"Đã tạo mã vận đơn thành công.")
        time.sleep(10)
time.sleep(30)
# Đóng trình duyệt Selenium
driver.quit()

