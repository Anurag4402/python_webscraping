#!/usr/bin/env python
# coding: utf-8

# In[10]:


import requests
from bs4 import BeautifulSoup


base_url = "https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_{}"

num_pages = 20


product_urls = []
product_names = []
product_prices = []
product_ratings = []
product_review_counts = []


for page_number in range(1, num_pages + 1):
    url = base_url.format(page_number)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    
    products = soup.find_all("div", {"data-component-type": "s-search-result"})

    for product in products:
        # Extract product URL
        product_url = "https://www.amazon.in" + product.find("a", class_="a-link-normal")["href"]
        product_urls.append(product_url)

        # Extract product name
        product_name = product.find("span", class_="a-text-normal").get_text()
        product_names.append(product_name)

        # Extract product price
        product_price = product.find("span", class_="a-offscreen").get_text()
        product_prices.append(product_price)

        # Extract product rating
        product_rating = product.find("span", class_="a-icon-alt")
        if product_rating:
            product_ratings.append(product_rating.get_text())
        else:
            product_ratings.append("No rating")

        # Extract number of reviews
        product_review_count = product.find("span", {"class": "a-size-base", "dir": "auto"})
        if product_review_count:
            product_review_counts.append(product_review_count.get_text())
        else:
            product_review_counts.append("No reviews")

# Print or process the scraped data
for i in range(len(product_urls)):
    print("Product URL:", product_urls[i])
    print("Product Name:", product_names[i])
    print("Product Price:", product_prices[i])
    print("Rating:", product_ratings[i])
    print("Number of Reviews:", product_review_counts[i])
    print("-" * 50)


# In[5]:


import requests
from bs4 import BeautifulSoup
import csv


# In[6]:


def scrape_product_data(url):
    headers = {
        "User-Agent": "Your User Agent String Here"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    description = soup.find("span", id="productTitle").get_text().strip()
    asin = soup.find("input", id="ASIN")["value"]
    product_description = soup.find("div", id="productDescription").get_text().strip()
    manufacturer = soup.find("a", id="bylineInfo").get_text().strip()

    return {
        "Description": description,
        "ASIN": asin,
        "Product Description": product_description,
        "Manufacturer": manufacturer
    }


# In[8]:


def scrape_product_data(url):
    headers = {
        "User-Agent": "Your User Agent String Here"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    description_element = soup.find("span", id="productTitle")
    description = description_element.get_text().strip() if description_element else "N/A"

    asin_element = soup.find("input", id="ASIN")
    asin = asin_element["value"] if asin_element else "N/A"

    product_description_element = soup.find("div", id="productDescription")
    product_description = product_description_element.get_text().strip() if product_description_element else "N/A"

    manufacturer_element = soup.find("a", id="bylineInfo")
    manufacturer = manufacturer_element.get_text().strip() if manufacturer_element else "N/A"

    return {
        "Description": description,
        "ASIN": asin,
        "Product Description": product_description,
        "Manufacturer": manufacturer
    }


# In[ ]:




