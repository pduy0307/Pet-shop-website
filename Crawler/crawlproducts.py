from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import re
import time
import csv
# Create an instance of Chrome driver
driver_path = "/usr/local/bin/"
browser = webdriver.Chrome(driver_path)
# Navigate to website Tiki.vn > Laptop category
category_links = ["https://tiki.vn/thuc-an-thu-cung/c53530", "https://tiki.vn/phu-kien-thu-cung/c53540"]
with open('products.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Category', 'Brand', 'Brand_name', 'Price', 'Images', 'Details', 'Description'])
    for category_link in category_links:
        browser.get(category_link)
        pagination = browser.find_element(By.CSS_SELECTOR, ".Pagination__Root-sc-cyke21-0.gNgpAR")
        last_page = int(pagination.find_elements(By.TAG_NAME, "a")[-2].text)
    # Select all product items by CSS Selector
        product_count = 0
        for page in range(1, last_page+1):
            url = f"{category_link}?page={page}"
            browser.get(url)
            time.sleep(5)
            list_product_link = []
            products = browser.find_elements(By.CSS_SELECTOR, ".product-item")
            for product in products:
                outer_html = product.get_attribute("outerHTML")
                product_link = re.search('href="(.*?)"', outer_html).group(1)
            # product_link = "https://" + product_link
                list_product_link.append(product_link)
                product_count += 1
                if product_count == 250:
                    break

    # Go to each product link
            for product_link in list_product_link:
                print("DEBUG: " + product_link)
                time.sleep(5)
            # Go to product link
                try:
                    browser.get("https://" + product_link)
                except:
                    browser.get("https://tiki.vn" + product_link)

        # Extract product information by CSS Selector
                product_title = browser.find_elements(By.CSS_SELECTOR, ".title")[1].text
                print("DEBUG TITLE: " + product_title)
                
                product_category_lv1 = browser.find_elements(By.XPATH, "/html/body/div[1]/div[1]/main/div[1]/div/div/a[4]")[0].text
                print("DEBUG CATEGORY LV1: " + product_category_lv1)
                product_category_lv2 = browser.find_elements(By.XPATH, "/html/body/div[1]/div[1]/main/div[1]/div/div/a[5]")[0].text
                print("DEBUG CATEGORY LV2: " + product_category_lv2)

                product_brand_name = browser.find_elements(By.XPATH, "//a[@data-view-id='pdp_details_view_brand']")[0].text
                print("DEBUG BRAND: " + product_brand_name)

                product_category = product_category_lv1 + '>' + product_category_lv2

        # Extract product price
                product_price_elements = browser.find_elements(By.CSS_SELECTOR, ".product-price__current-price")
                if len(product_price_elements) > 0:
                    product_price = product_price_elements[0].text
                else:
                    product_price = browser.find_elements(By.CSS_SELECTOR, ".styles__Price-sc-6hj7z9-1.jgbWJA")[0].text
                product_price = re.search('^[\\d|\\.|\\,]+', product_price).group(0)
                print("DEBUG PRICE: " + product_price)
        # Extract product images
                product_images = []
                image_elements = browser.find_elements(By.CSS_SELECTOR, ".review-images__list .WebpImg__StyledImg-sc-h3ozu8-0.fWjUGo")
                for image_element in image_elements:
                    image_url = image_element.get_attribute("src")
                    product_images.append(image_url)
                print("DEBUG IMAGES: " + str(product_images))

        # Extract product details
                product_details = {}
                details_elements = browser.find_elements(By.CLASS_NAME, "content.has-table")
                for details_element in details_elements:
                    rows = details_element.find_elements(By.TAG_NAME, "tr")
                    for row in rows:
                        cells = row.find_elements(By.TAG_NAME, "td")
                        key = cells[0].text.strip()
                        try:
                            value = cells[1].text.strip()
                            product_details[key] = value
                        except:
                            continue
        
                print("DEBUG DETAILS: " + str(product_details))
        
        # Extract product description
                product_description = browser.find_element(By.XPATH,'//div[contains(@class, "ToggleContent__View-sc-1dbmfaw-0 wyACs")]').get_attribute("innerHTML")
                print("DEBUG DESCRIPTION: " + product_description)
        
                time.sleep(5)
                writer.writerow([product_title, product_category, 'Brand', product_brand_name, product_price, ', '.join(product_images), product_details, product_description])
            if product_count == 250:
                break
# Close the browser
browser.quit()