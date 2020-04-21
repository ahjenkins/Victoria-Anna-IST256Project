#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
show = input("Enter a tv show:")
url = "https://api.themoviedb.org/3/search/tv"
options = {"api_key": "ec48e90645213e27889dec45938e0d35", "query": show}
response = requests.get(url, params = options)
response.json()


# In[ ]:




