# Test bằng postman
# Get/post tuỳ cái mình mong muốn
# Đưa url vào vd: localhost/lab2metmoi/wp-json/wc/v3/products
# Bước xác thực thì chọn auth 1.0 thay username pw bằng comsumer_key và consumer_secret

import csv
import time
from woocommerce import API

def is_category_exists(category_name):
    categories = wcapi.get("products/categories").json()
    for i in categories:
        print(i["name"])
    for category in categories:
        if (category["name"]) == category_name:
            return category["id"]
    return None

# Xác thực
wcapi = API(
    # Thay bằng localhost của máy cá nhân là được
    url="http://localhost/lab2metmoi/",
    # Sửa theo api tạo ra từ wc
    consumer_key="ck_293699d389c5b5a39331d75c05a66f3297b3dcdb",
    consumer_secret="cs_336bb94878f09692a388c6b3b2127fea9cd39239",
    wp_api=True,
    version="wc/v3",
)

# Xoá sản phẩm khi số lượng = 0 - hết hàng 
products = wcapi.get("products").json() 
for product in products:
    if (product["stock_quantity"] == 0):
        url = "products/" + str(product["id"])
        wcapi.delete(url , params={"force": False})

# Thêm/Sửa sản phẩm từ file csv
csv_file = "/Users/luonh/Dev/Wordpress/products.csv"

    # Đọc dữ liệu từ file CSV và thêm sản phẩm
import csv

with open(csv_file, "r", newline="") as file:
    reader = csv.DictReader(file)
    products = wcapi.get("products").json()
    existing_product_names = [product["name"] for product in products]
    # cates = wcapi.get("products/categories").json()
    # for cate in cates:
    #     print(cate["name"])

    for row in reader:
        name = row["Title"]
        brand = row["Brand"]
        price = row["Price"]
        images = row["Images"].split(",")
        image_data = [{"src": url.strip()} for url in images]
        short_description = row["Details"]
        description = row["Description"]
        
        # Kiểm tra trùng lặp dựa trên tên sản phẩm
        if name in existing_product_names:
            for product in products:
                if product["name"] == name:
                    existing_price = float(product["regular_price"].replace('.', '').replace(',', ''))
                    new_price = float(price.replace('.', '').replace(',', ''))
                    if existing_price != new_price:
                        print("Giá sản phẩm đã thay đổi:", product["regular_price"], "->", price)
                        # Cập nhật giá sản phẩm
                    else:
                        print("Giá sản phẩm không thay đổi.")
                    break
        else:
            existing_category_id = is_category_exists(brand)
            if existing_category_id:
                category_id = existing_category_id
                print("danh muc sản phẩm đã tồn tại")
            else:
                brand_data = {
                    "name": brand.strip(),
                }
                print("tạo mới danh mục")
                category = wcapi.post("products/categories", brand_data)
                print(brand_data)
                category_id = (category.json()).get('id')
            print(category_id)
            time.sleep(5)
            product_data = {
                "name": name,
                "categories": [
                    {
                        "id": category_id
                    }
                ],
                "regular_price": price,
                "images": image_data,
                "short_description": short_description,
                "description": description,
            }
            response = wcapi.post("products", product_data)
            print(f"Sản phẩm '{name}' đã được thêm thành công.")

