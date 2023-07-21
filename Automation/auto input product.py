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
driver.get("https://famipet.top/wp-admin/edit.php?post_type=product")

# Đăng nhập vào tài khoản quản trị WooCommerce
username = driver.find_element(By.ID, "user_login")
password = driver.find_element(By.ID, "user_pass")
username.send_keys("famipet")
password.send_keys("famipet")
driver.find_element(By.ID, "wp-submit").click()

time.sleep(5)

# Click vào submenu "Nhập khẩu"
driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[6]/a[2]").click()
time.sleep(5)

# Tìm và nhập đường dẫn đến file CSV
file_input = driver.find_element(By.CSS_SELECTOR, 'input[type="file"]')
file_input.send_keys("C:/Users/computer/Downloads/project/products.csv")
time.sleep(5)
driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

time.sleep(5)
name = driver.find_element(By.NAME, "map_to[0]")
category = driver.find_element(By.NAME, "map_to[1]")
brand = driver.find_element(By.NAME, "map_to[2]")
brand_name = driver.find_element(By.NAME, "map_to[3]")
price = driver.find_element(By.NAME, "map_to[4]")
images = driver.find_element(By.NAME, "map_to[5]")
short_details = driver.find_element(By.NAME, "map_to[6]")


name.send_keys("Tên")
category.send_keys("Danh mục")
brand.send_keys("Tên thuộc tính")
brand_name.send_keys("Giá trị thuộc tính")
price.send_keys("Giá bán thường")
images.send_keys("Hình ảnh")
short_details.send_keys("Mô tả ngắn")


time.sleep(10)

# Bấm nút "Chạy trình nhập"
driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
print("Đã import thành công")

# Đợi cho quá trình nhập khẩu hoàn thành
time.sleep(30)
# Đóng trình duyệt Selenium
driver.quit()

