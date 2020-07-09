from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import csv

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=chrome_options)


with open("books.csv", "w") as csvfile:
  csv_writer = csv.writer(csvfile)
  csv_writer.writerow(["name", "price"])

  driver.get("http://books.toscrape.com/")
  articles = driver.find_elements_by_class_name("product_pod")
  for a in articles:
    name_container = a.find_element_by_tag_name("h3")
    name = name_container.find_element_by_tag_name("a").get_attribute("title")
    print(name)
    price_container = a.find_element_by_class_name("product_price")
    price = price_container.find_element_by_class_name("price_color").text
    print(price)
    csv_writer.writerow([name, price])
csvfile.close()
