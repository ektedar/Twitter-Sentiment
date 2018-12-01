'''
This Python code will scrape the Twitter Account given to it.  This will include information such as User bio and Tweets
@author: Ektedar Alam
'''

import urllib
import urllib.request
import bs4
from textblob import TextBlob as tb

USER_URL = "https://www.twitter.com/Ektadizzy"
USER_PAGE = urllib.request.urlopen(USER_URL)

# Variable Initializations for readability
def get_user_info(page):
    soup = bs4.BeautifulSoup(page, 'html.parser')
    handle = soup.title.text
    bio = soup.find('div', {'class':'ProfileHeaderCard'}).find('p').text
    location = str(soup.find('div', {'class':'ProfileHeaderCard-location'}).text).replace("\n", "").replace(" ", "")
    return handle, bio, location

# Calcualte sentiment of whatever string is being passed
def textblob_sentiment(tweet):
    blob = tb(tweet)
    sentiment = blob.sentiment[0]
    return sentiment

# Get Tweets from the user
def get_tweets(page):
    soup = bs4.BeautifulSoup(page, 'html.parser')
    for content in soup.findAll('div', {'class':'content'}):
        tweet = content.find('p').text
        sentiment = textblob_sentiment(tweet)
        print("TWEET: " + str(tweet) + " SENTIMENT: "+ str(sentiment))
       
if __name__ == "__main__":
    # user_handle, user_bio, user_location = get_user_info(USER_PAGE)
    get_tweets(USER_PAGE)