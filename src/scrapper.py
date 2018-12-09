'''
This Python code will scrape the Twitter Account given to it.  This will include information such as User bio and Tweets
'''
import time
import urllib
import urllib.request
import argparse
import bs4
from textblob import TextBlob as tb

# Variable Initializations for readability
def get_user_info(page):
    soup = bs4.BeautifulSoup(page, 'html.parser')
    handle = soup.title.text
    bio = soup.find('div', {'class':'ProfileHeaderCard'}).find('p').text
    location = str(soup.find('div', {'class':'ProfileHeaderCard-location'}).text).replace("\n", "").replace(" ", "")
    return handle, bio, location

# Get Tweets from the user
def get_tweets(content):
    tweet = content.find('p').text
    return tweet        

# Get the twitter page of the user as added through the CMD line
def main(user):
    user_url = f"https://www.twitter.com/{user}"
    open_url = urllib.request.urlopen(user_url)
    soup = bs4.BeautifulSoup(open_url, 'html.parser')
    for content in soup.findAll('div', {'class':'content'}):
        tweets = get_tweets(content)
        print(tweets)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="This file scraps the twitter profile of the provided user and retrieves their tweets")
    parser.add_argument('--user', required=True, help='The Twitter handle of the twitter user')
    arg = parser.parse_args()
    user = str(arg.user).replace("@", "")
    main(user)