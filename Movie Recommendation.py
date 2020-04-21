#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests 
url = "https://tastedive.com/api/similar"
movie = input("Enter a movie:")
options = {'q': f'movie:{movie}', 'type': 'movie', 'info': 1, 'k': '365858-project-GTOG8MVJ'}
response = requests.get(url, params = options)
recommendation = response.json()
print(recommendation['Similar']['Results'][0]['Name'])
print(recommendation['Similar']['Results'][0]['wTeaser'])
print(recommendation['Similar']['Results'][1]['Name'])
print(recommendation['Similar']['Results'][1]['wTeaser'])
print(recommendation['Similar']['Results'][2]['Name'])
print(recommendation['Similar']['Results'][2]['wTeaser'])

