import requests
from bs4 import BeautifulSoup

URL = "https://www.woolandcompany.com/collections/cascade-pacific"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(class_="collection-row")

products = results.find_all("a", class_="product-thumbnail")

for product in products:
    img_element = product.find("img")
    img_src = img_element.get("src")
    img_name = img_src.replace("//www.woolandcompany.com/cdn/shop/files/","")[:-23]


    title_element = product.find(class_="product-thumbnail--title")
    title = title_element.text.strip()
    

    csv_row = title + "," + img_name

    print(csv_row)

