from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
def get_title(soup):
    try:
        title = soup.find("span",attrs={'id':'productTitle'})
        title_value = title.text
        title_string = title_value.strip()
    except AttributeError:
        title_string = " "
    return title_string
def get_price(soup):
    try:
        price = soup.find("span",attrs={'class':'a-price-whole'})
        price_value = price.text
        price_string = price_value.strip()
    except AttributeError:
        price_string = " "
    return price_string
    
    
URL = "https://www.amazon.in/s?k=wallet&crid=1MMR29HNFU374&sprefix=%2Caps%2C489&ref=nb_sb_ss_recent_3_0_recent"

HEADERS = ({'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
            'Accepted-Language' : 'en-US, en;q=0.5'})

webpage = requests.get(URL,headers=HEADERS) 

soup = BeautifulSoup(webpage.content,"html.parser")


links = soup.find_all("a",attrs={'class':'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})


links_list = []
for link in links:
            links_list.append(link.get('href'))

d = {"title":[], "price":[]}


for link in links_list:
    try:
        productlist = "https://www.amazon.in" + link
    except ConnectionError:
        cleaned_link = link.replace("https://", "")
        productlist = "https://www.amazon.in" + cleaned_link
    inside_webpage = requests.get(productlist,headers=HEADERS)
    new_soup = BeautifulSoup(inside_webpage.content, "html.parser")

    d['title'].append(get_title(new_soup))
    d['price'].append(get_price(new_soup))

    
    amazon_df = pd.DataFrame.from_dict(d)
    amazon_df = amazon_df.dropna(subset=['title'])
    amazon_df.to_csv("amazon_data.csv", header=True, index=False)