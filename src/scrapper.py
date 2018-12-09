'''
This Python code will scrape the Twitter Account given to it.  This will include information such as User bio and Tweets
'''
import time
import urllib
import urllib.request
import argparse
import bs4
from selenium import webdriver
from textblob import TextBlob as tb

# Variable Initializations for readability
def get_user_info(page):
    soup = bs4.BeautifulSoup(page, 'html.parser')
    handle = soup.title.text
    bio = soup.find('div', {'class':'ProfileHeaderCard'}).find('p').text
    location = str(soup.find('div', {'class':'ProfileHeaderCard-location'}).text).replace("\n", "").replace(" ", "")
    return handle, bio, location

# Generate an infinite scroll of the provided page
def infinite_scroll(page):
    print(page)
    driver = webdriver.Chrome()
    print("Starting")
    driver.get(page)
    scroll_page_time = 1.5
    last_height = driver.execute_script("return document.body.scrollHeight")
    while(True):
        print(last_height)
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        time.sleep(scroll_page_time)
        new_height = driver.execute_script("return document.body.scrollHeight")
        print(new_height, last_height)
        if new_height == last_height:
            break
        last_height = new_height

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
        # sentiment = textblob_sentiment(tweet)
        print(tweet)
        # print(sentiment)

# Get the twitter page of the user as added through the CMD line
def main(user):
    user_url = f"https://www.twitter.com/{user}"
    full_page = infinite_scroll(user_url)
    user_page = urllib.request.urlopen(full_page)
    get_tweets(user_page)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="This file scraps the twitter profile of the provided user and retrieves their tweets")
    parser.add_argument('--user', required=True, help='The Twitter handle of the twitter user')
    arg = parser.parse_args()
    user = str(arg.user).replace("@", "")
    main(user)