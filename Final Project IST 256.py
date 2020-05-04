#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().system(' pip install emoji')


# In[ ]:



import requests
import emoji


# In[3]:


def exchangeRate(currency, media_price): #decide if it needs a parameter
    try: 
        currency_API_key = '14f82688f78443d789d8268e'
        url = f"https://prime.exchangerate-api.com/v5/{currency_API_key}/latest/USD"
        response = requests.get(url)
        json_format = response.json()
        base = json_format['base'] #base currency
        conversions = json_format['conversion_rates']#list of conversion rates
        if currency not in conversions:
            print("Currency not found. ")
        elif currency in conversions:
            price = media_price
            exchange_rate = conversions[currency.upper()]
            conversion = float(price*exchange_rate)
            conversion_price = "{:.2f}".format(conversion)
            return conversion_price
    except json.decoder.JSONDecodeError as e: 
        return ("ERROR: Cannot decode the response into json")

    # response not ok
    except requests.exceptions.HTTPError as e:
        return("ERROR: Response from ", url, 'was not ok.')

    # internet is broken
    except requests.exceptions.RequestException as e: 
        return("ERROR: Cannot connect to ", url)


# In[4]:



def getMovieID(movie):
    try: 
        searchMovie_endpoint = '/search/movie?'
        url = f"https://api.themoviedb.org/3{searchMovie_endpoint}"
        query1 = { 'api_key' : 'af0e78b67a94ac0b4b6e41b1345d3c00', 'query' : movie }
        response = requests.get(url, params=query1)
        result = response.json()
        if result['total_results'] == 0:
            print('No results found. Please restart.')
        movie_id = result['results'][0]['id'] #gets movie_id
        return movie_id
    except json.decoder.JSONDecodeError as e: 
        return ("ERROR: Cannot decode the response into json")

    # response not ok
    except requests.exceptions.HTTPError as e:
        return("ERROR: Response from ", url, 'was not ok.')

    # internet is broken
    except requests.exceptions.RequestException as e: 
        return("ERROR: Cannot connect to ", url)
def movieReviews(movieID):
    try:
        movie_id = getMovieID(movie)
        reviews_endpoint = f"/movie/{movie_id}/reviews"
        url2 = f'https://api.themoviedb.org/3{reviews_endpoint}'
        query2 = { 'api_key' : 'af0e78b67a94ac0b4b6e41b1345d3c00' }
        response1 = requests.get(url2, params=query2)
        reviews = response1.json()
        if reviews['total_results'] == 0:
            print('This movie has no reviews')
        list_of_reviews = reviews['results']
        return list_of_reviews #loop later
    except json.decoder.JSONDecodeError as e: 
        return ("ERROR: Cannot decode the response into json")

    # response not ok, borrowed from http lab
    except requests.exceptions.HTTPError as e:
        return("ERROR: Response from ", url, 'was not ok.')

    # internet is broken, borrowed from http lab
    except requests.exceptions.RequestException as e: 
        return("ERROR: Cannot connect to ", url)


# In[5]:


def getShowID(show):
    try:
        url = 'https://api.themoviedb.org/3/search/tv' #TV show search URL
        query = { 'api_key' : 'af0e78b67a94ac0b4b6e41b1345d3c00', 'query': show}
        response = requests.get(url, params = query)
        result = response.json()
        if result['total_results'] == 0:
            print('No results found.  Please restart.')
        tv_id = result['results'][0]['id'] #get id for TV show
        return tv_id
    except json.decoder.JSONDecodeError as e: 
        return ("ERROR: Cannot decode the response into json")

    # response not ok, borrowed from http lab
    except requests.exceptions.HTTPError as e:
        return("ERROR: Response from ", url, 'was not ok.')

    # internet is broken, borrowed from http lab
    except requests.exceptions.RequestException as e: 
        return("ERROR: Cannot connect to ", url)
def showReviews(tvID):
    try:
        tv_id = getShowID(show)
        tv_review_endpoint = f'/tv/{tv_id}/reviews'
        url2 = f'https://api.themoviedb.org/3{tv_review_endpoint}' #tv show review URL
        query2 = { 'api_key' : 'af0e78b67a94ac0b4b6e41b1345d3c00'}
        response2 = requests.get(url2, params=query2)
        reviews = response2.json()
        if reviews['total_results'] == 0:
            print('This show has no reviews.')
        list_of_reviews = reviews['results']
        return list_of_reviews
    except json.decoder.JSONDecodeError as e: 
        return ("ERROR: Cannot decode the response into json")

    # response not ok, borrowed from http lab
    except requests.exceptions.HTTPError as e:
        return("ERROR: Response from ", url, 'was not ok.')

    # internet is broken, borrowed from http lab
    except requests.exceptions.RequestException as e: 
        return("ERROR: Cannot connect to ", url)


# In[7]:


def getSentiment(text):
    try:
        url = 'http://text-processing.com/api/sentiment/'
        options = { 'text' : text }
        response = requests.post(url, data=options)
        result = response.json()
        sentiment = result['label']
        return sentiment
    except json.decoder.JSONDecodeError as e: 
        return ("ERROR: Cannot decode the response into json")

    # response not ok, borrowed from http lab
    except requests.exceptions.HTTPError as e:
        return("ERROR: Response from ", url, 'was not ok.')

    # internet is broken, borrowed from http lab
    except requests.exceptions.RequestException as e: 
        return("ERROR: Cannot connect to ", url)


# In[9]:

def showMoviePrices(media):#can readjust later to what the user wants to see the price for and connect it to the movie or show they already entered in
    try:
        url = "https://itunes.apple.com/search?parameterkeyvalue."
        options = {'term': media, 'country': 'US', 'media':'movie'}
        response = requests.get(url, params = options)
        price = response.json()
        movie_price = 0  
        option = input("Do you want to buy or rent this movie?").lower()
        if option == 'buy':
            quality = input("Do you want to buy this movie in HD or SD?").upper()
            if quality == 'HD':
                movie_price = float(price['results'][0]['trackHdPrice'])
            elif quality == 'SD':
                movie_price = float(price['results'][0]['trackPrice'])
            else:
                movie_price = "Please retry and enter 'HD' or 'SD.'"
        elif option == 'rent':
            quality = input("Do you want to rent this movie in HD or SD?").upper()
            if quality == 'HD':
                movie_price = float(price['results'][0]['trackHdRentalPrice'])
            elif quality == 'SD':
                movie_price = float(price['results'][0]['trackRentalPrice'])
            else: 
                movie_price = "Please retry and enter 'HD' or 'SD.'"
        else:
            movie_price = "Please retry and enter 'buy' or 'rent.'"
        return movie_price
    except json.decoder.JSONDecodeError as e: 
        return ("ERROR: Cannot decode the response into json")

    # response not ok, borrowed from http lab 
    except requests.exceptions.HTTPError as e:
        return("ERROR: Response from ", url, 'was not ok.')

    # internet is broken, borrowed from http lab
    except requests.exceptions.RequestException as e: 
        return("ERROR: Cannot connect to ", url)

def showShowPrices(show):
    try:
        url = "https://itunes.apple.com/search?parameterkeyvalue."
        data = {'term': show, 'country': 'US', 'media':'tvShow'}
        tv_response = requests.get(url, params = data)
        tv_price = tv_response.json()
        price = 0
        option = input("Enter 'episode' if you want to buy one episode or 'season' for the whole season.").lower()
        if option == 'episode':
            price = float(tv_price['results'][0]['trackPrice'])
        elif option == 'season':
             price = float(tv_price['results'][0]['collectionPrice'])
        else:
            price = "Please retry and enter 'episode' or 'season.'"
        return price
    except json.decoder.JSONDecodeError as e: 
        return ("ERROR: Cannot decode the response into json")

    # response not ok, borrowed from http lab
    except requests.exceptions.HTTPError as e:
        return("ERROR: Response from ", url, 'was not ok.')

    # internet is broken, borrowed from http lab
    except requests.exceptions.RequestException as e: 
        return("ERROR: Cannot connect to ", url)


def movieRecommendations(movie):
    try:
        url = "https://tastedive.com/api/similar"
        options = {'q': f'movie:{movie}', 'type': 'movie', 'info': 1, 'k': '365858-project-GTOG8MVJ'}
        response = requests.get(url, params = options)
        recommendation = response.json()
        return recommendation
    except json.decoder.JSONDecodeError as e: 
        return ("ERROR: Cannot decode the response into json")

    # response not ok,borrowed from http lab
    except requests.exceptions.HTTPError as e:
        return("ERROR: Response from ", url, 'was not ok.')

    # internet is broken, borrowed from http lab
    except requests.exceptions.RequestException as e: 
        return("ERROR: Cannot connect to ", url)
def showRecommendations(show): 
    try:
        url = "https://tastedive.com/api/similar"
        options = {'q': f'show:{show}', 'type': 'show', 'info': 1, 'k': '365858-project-GTOG8MVJ'}
        response = requests.get(url, params = options)
        recommendation = response.json()
        return recommendation
    except json.decoder.JSONDecodeError as e: 
        return ("ERROR: Cannot decode the response into json")

    # response not ok, borrowed from http lab
    except requests.exceptions.HTTPError as e:
        return("ERROR: Response from ", url, 'was not ok.')

    # internet is broken, borrowed from http lab
    except requests.exceptions.RequestException as e: 
        return("ERROR: Cannot connect to ", url)



# # Program

# In[12]:


print('Welcome to Movies for Me')
print("This program allows you to search a movie or TV show and read its reviews.\nWe do sentiment analysis over the reviews and tell you how much the movie costs on iTunes.\nWe also recommend similar movies or TV shows to your search.\n")



while True:
    decision = input("Would you like to search a movie or show? Type 'quit' to quit.").lower()
    if decision == 'movie': #create if statement if the movie was not found
        find_title = input('Enter a movie: ') #assign to another variable later
        movie = find_title
        title_id = getMovieID(movie)
        movie_reviews = movieReviews(title_id)
        for review in movie_reviews:
            sentiment = getSentiment(review['content'])
            if sentiment == 'pos':
                print(review['author'], 'gave a', emoji.emojize(':thumbs_up:'), 'review:')
            elif sentiment =='neg':
                print(review['author'], 'gave a', emoji.emojize(':thumbs_down:'), 'review:')
            print(review['content'])
            

        movie_price = showMoviePrices(find_title)
        if movie_price != "Please retry and enter 'HD' or 'SD.'" and movie_price != "Please retry and enter 'buy' or 'rent.'":
            currency = input("Enter a currency (ex: EUR): ")
            converted_price = exchangeRate(currency, movie_price)
            print(f"To purchase from iTunes in {currency.upper()} is {converted_price}.")     
        else: 
            print(movie_price)

        similar = input("Do you want to see similar movies?").lower()
        if similar == 'yes': # if user wants recommendations
            recommendation = movieRecommendations(find_title)
            print(f"Movie 1: {recommendation['Similar']['Results'][0]['Name']}\n")
            print(f"Summary: {recommendation['Similar']['Results'][0]['wTeaser']}\n")
            print(f"Movie 2: {recommendation['Similar']['Results'][1]['Name']}\n")
            print(f"Summary: {recommendation['Similar']['Results'][1]['wTeaser']}\n")
            print(f"Movie 3: {recommendation['Similar']['Results'][2]['Name']}\n")
            print(f"Summary: {recommendation['Similar']['Results'][2]['wTeaser']}\n")
            decision = input("Would you like to search a movie or show? Type 'quit' to quit.").lower()
        
        elif similar == 'no': # if user doesn't want recommendations
            decision = input("Would you like to search a movie or show? Type 'quit' to quit.").lower()
            continue


    elif decision == 'show': #create if statement if the show was not found
        find_title = input('Enter a tv show: ')
        show = find_title
        title_id = getShowID(show)
        tv_reviews = showReviews(title_id)
        for review in tv_reviews:
            sentiment = getSentiment(review['content'])
            if sentiment == 'pos':
                  print(review['author'], 'gave a', emoji.emojize(':thumbs_up:'), 'review:')
            elif sentiment =='neg':
                print(review['author'], 'gave a', emoji.emojize(':thumbs_down:'), 'review:')
            print(review['content'])

        show_price = showShowPrices(find_title)
        if show_price != "Please retry and enter 'episode' or 'season.'":
            currency = input("Enter a currency (ex: EUR): ")
            converted_price = exchangeRate(currency, show_price)
            print(f"To purchase from iTunes in {currency.upper()} is {converted_price}.")  
        else:
            print(show_price)

        similar = input("Do you want to see similar tv shows?").lower()
        if similar == 'yes': # if user wants recommendations
            recommendation = showRecommendations(find_title)
            print(f"TV Show 1: {recommendation['Similar']['Results'][0]['Name']}\n")
            print(f"Summary: {recommendation['Similar']['Results'][0]['wTeaser']}\n")
            print(f"TV Show 2: {recommendation['Similar']['Results'][1]['Name']}\n")
            print(f"Summary: {recommendation['Similar']['Results'][1]['wTeaser']}\n")
            print(f"TV Show 3: {recommendation['Similar']['Results'][2]['Name']}\n")
            print(f"Summary: {recommendation['Similar']['Results'][2]['wTeaser']}\n")
            decision = input("Would you like to search a movie or show? Type 'quit' to quit.").lower()
        
        elif similar == 'no': # if user doesn't want recommendations
            decision = input("Would you like to search a movie or show? Type 'quit' to quit.").lower()
            continue
                  

    elif decision != 'movie' or decision != 'show' and decision != 'quit':
        print("Please restart and enter 'movie' or 'show'.")
 print("Thank you for using 'Movies for Me.'")
    


# ![](movies_for_me.jpg)

# In[ ]:




