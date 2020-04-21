#!/usr/bin/env python
# coding: utf-8

# In[13]:


import requests 
url = "https://itunes.apple.com/search?parameterkeyvalue."
media = input("Enter a movie title:")
options = {'term': media, 'country': 'US', 'media':'movie'}
response = requests.get(url, params = options)
price = response.json()
print(f"Price to buy in SD: {price['results'][0]['trackPrice']}")
print(f"Price to rent in SD: {price['results'][0]['trackRentalPrice']}")
print(f"Price to buy in HD: {price['results'][0]['trackHdPrice']}")
print(f"Price to rent in HD: {price['results'][0]['trackHdRentalPrice']}")


# In[29]:


import requests 
url = "https://itunes.apple.com/search?parameterkeyvalue."
show = input("Enter a tv show:")
data = {'term': show, 'country': 'US', 'media':'tvShow'}
tv_response = requests.get(url, params = data)
tv_price = tv_response.json()
print(f"Price for whole season: {tv_price['results'][0]['collectionPrice']}")
print(f"Price for one episode: {tv_price['results'][0]['trackPrice']}")

