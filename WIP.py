#!/usr/bin/env python
# coding: utf-8

# In[ ]:



import requests


# In[3]:


def exchangeRate(): #decide if it needs a parameter
    currency_API_key = '14f82688f78443d789d8268e'
    country_code = input('Enter a currency: ')
    url = f"https://prime.exchangerate-api.com/v5/{currency_API_key}/latest/{country_code}"
    response = requests.get(url)
    json_format = response.json()
    base = json_format['base'] #base currency
    conversions = json_format['conversion_rates'] #list of conversion rates
    currency = input('Enter the currency you want (ex: EUR): ')
    price = 20 #CHANGE LATER
    exchange_rate = conversions[currency.upper()]
    conversion = float(price*exchange_rate)
    return conversion


# In[4]:


def getMovieID(movie):
    searchMovie_endpoint = '/search/movie?'
    url = f"https://api.themoviedb.org/3{searchMovie_endpoint}"
    query1 = { 'api_key' : 'af0e78b67a94ac0b4b6e41b1345d3c00', 'query' : movie }
    response = requests.get(url, params=query1)
    result = response.json()
    movie_id = result['results'][0]['id'] #gets movie_id
    return movie_id
def movieReviews(movieID):
    movie_id = getMovieID(movie)
    reviews_endpoint = f"/movie/{movie_id}/reviews"
    url2 = f'https://api.themoviedb.org/3{reviews_endpoint}'
    query2 = { 'api_key' : 'af0e78b67a94ac0b4b6e41b1345d3c00' }
    response1 = requests.get(url2, params=query2)
    reviews = response1.json()
    list_of_reviews = reviews['results']
    return list_of_reviews #loop later


# In[5]:


def getShowID(show):
    url = 'https://api.themoviedb.org/3/search/tv' #TV show search URL
    query = { 'api_key' : 'af0e78b67a94ac0b4b6e41b1345d3c00', 'query': show}
    response = requests.get(url, params = query)
    result = response.json()
    tv_id = result['results'][0]['id'] #get id for TV show
    return tv_id
def showReviews(tvID):
    tv_id = getShowID(show)
    tv_review_endpoint = f'/tv/{tv_id}/reviews'
    url2 = f'https://api.themoviedb.org/3{tv_review_endpoint}' #tv show review URL
    query2 = { 'api_key' : 'af0e78b67a94ac0b4b6e41b1345d3c00'}
    response2 = requests.get(url2, params=query2)
    reviews = response2.json()
    list_of_reviews = reviews['results']
    return list_of_reviews


# In[7]:


def getSentiment(text):
    url = 'http://text-processing.com/api/sentiment/'
    options = { 'text' : text }
    response = requests.post(url, data=options)
    result = response.json()
    sentiment = result['label']
    return sentiment


# In[9]:


def showMoviePrices(): #can readjust later to what the user wants to see the price for and connect it to the movie or show they already entered in
    url = "https://itunes.apple.com/search?parameterkeyvalue."
    media = input("Enter a movie title:")
    options = {'term': media, 'country': 'US', 'media':'movie'}
    response = requests.get(url, params = options)
    price = response.json()
    buy_SD = price['results'][0]['trackPrice']
    rent_SD = price['results'][0]['trackRentalPrice']
    buy_HD = price['results'][0]['trackHdPrice']
    rent_HD = price['results'][0]['trackHdRentalPrice']
    return [buy_SD, rent_SD, buy_HD, rent_HD]
def showShowPrices():
    url = "https://itunes.apple.com/search?parameterkeyvalue."
    show = input("Enter a tv show:")
    data = {'term': show, 'country': 'US', 'media':'tvShow'}
    tv_response = requests.get(url, params = data)
    tv_price = tv_response.json()
    season_price = tv_price['results'][0]['collectionPrice']
    episode_price = tv_price['results'][0]['trackPrice']
    return [season_price, episode_price]


def movieRecommendations(movie):
    url = "https://tastedive.com/api/similar"
    options = {'q': f'movie:{movie}', 'type': 'movie', 'info': 1, 'k': '365858-project-GTOG8MVJ'}
    response = requests.get(url, params = options)
    recommendation = response.json()
    return recommendation
def showRecommendations(show): 
    url = "https://tastedive.com/api/similar"
    options = {'q': f'show:{show}', 'type': 'show', 'info': 1, 'k': '365858-project-GTOG8MVJ'}
    response = requests.get(url, params = options)
    recommendation = response.json()
    return recommendation



# # Program

# In[12]:


# print('Welcome to Movies for Me')
# print('This program allows you to search a movie or TV show and read its reviews.
    #We do sentiment analysis over the reviews and tell you how much the movie costs on iTunes.  
    #We also recommend similar movies or TV shows to your search.')


#ask for currency abbreviation
# user_currency = input('Enter the abbreviation of your preferred currency: ') #will use in an if statement later

#ask user for a movie or tv show title
decision = input('Would you like to search a movie or show? ').lower()
if decision == 'movie': #create if statement if the movie was not found
    find_title = input('Enter a movie: ') #assign to another variable later
    movie = find_title
    title_id = getMovieID(movie)
    movie_reviews = movieReviews(title_id)
    for review in movie_reviews:
        sentiment = getSentiment(review['content'])
        print(review['author'], 'gave a', sentiment, 'review:')
        print(review['content'])
    
    
        
    similar = input("Do you want to see similar movies?").lower()
    if similar == 'yes':
        recommendation = movieRecommendations(find_title)
        print(f"Movie 1: {recommendation['Similar']['Results'][0]['Name']}\n")
        print(f"Summary: {recommendation['Similar']['Results'][0]['wTeaser']}\n")
        print(f"Movie 2: {recommendation['Similar']['Results'][1]['Name']}\n")
        print(f"Summary: {recommendation['Similar']['Results'][1]['wTeaser']}\n")
        print(f"Movie 3: {recommendation['Similar']['Results'][2]['Name']}\n")
        print(f"Summary: {recommendation['Similar']['Results'][2]['wTeaser']}\n")
    
elif decision == 'show': #create if statement if the show was not found
    find_title = input('Enter a tv show: ')
    show = find_title
    title_id = getShowID(show)
    tv_reviews = showReviews(title_id)
    for review in tv_reviews:
        sentiment = getSentiment(review['content'])
        print(review['author'], 'gave a', sentiment, 'review:')
        print(review['content'])
              
    
    similar = input("Do you want to see similar tv shows?").lower()
    if similar == 'yes':
        recommendation = showRecommendations(find_title)
        print(f"TV Show 1: {recommendation['Similar']['Results'][0]['Name']}\n")
        print(f"Summary: {recommendation['Similar']['Results'][0]['wTeaser']}\n")
        print(f"TV Show 2: {recommendation['Similar']['Results'][1]['Name']}\n")
        print(f"Summary: {recommendation['Similar']['Results'][1]['wTeaser']}\n")
        print(f"TV Show 3: {recommendation['Similar']['Results'][2]['Name']}\n")
        print(f"Summary: {recommendation['Similar']['Results'][2]['wTeaser']}\n")

elif decision != 'movie' or decision != 'show':
    print("Please restart and enter 'movie' or 'show'.")
    


# In[ ]:




