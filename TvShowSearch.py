#!/usr/bin/env python
# coding: utf-8

# In[7]:


import requests
show = input("Enter a tv show:")
url = "https://api.themoviedb.org/3/search/tv"
options = {"api_key": "ec48e90645213e27889dec45938e0d35", "query": show}
response = requests.get(url, params = options)
tv_show = response.json()

print(f"TV Show: {tv_show['results'][0]['name']}")
print(f"About: {tv_show['results'][0]['overview']}")


# In[ ]:




