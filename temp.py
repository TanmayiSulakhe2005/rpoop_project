#print(f"Status Code: {webpage.status_code}")
#print("Webpage Content:")
#print(webpage.content[:200]) 
#print(soup)
#link1 = links[0].get('href')

#productlist = "https://www.amazon.in" + link1
#inside_webpage = requests.get(productlist,headers=HEADERS)
#new_soup = BeautifulSoup(inside_webpage.content,"html.parser")
#new_soup.find("span",attrs={'id':'productTitle'}).text.strip()

#print(new_soup.find("span",attrs={'id':'productTitle'}).text.strip())
#print(new_soup.find("span",attrs={'class':'a-price-whole'}).text.strip())


#amazon_df['title'].replace('', np.nan, inplace=True)