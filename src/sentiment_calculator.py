'''
This python file will calculate the Sentiment of whatever text is provided.  
The following sentiments calculators are currently being utilized:
    TextBlob
    Vader Sentiment
    AWS Comprehend (tentative)
'''
import scrapper
import argparse
import pprint
from textblob import TextBlob as tb

# Returns a tweet with calculated sentiment
def text_blob_sentiment(tweet):
    blob = tb(tweet)
    sentiment = blob.sentiment[0]
    return sentiment

def main(user):
    tweet_dict = scrapper.get_tweets(user)
    for k in tweet_dict:
        tweet_dict[k] = text_blob_sentiment(k)
    pprint.pprint(tweet_dict)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="This file returns a dictionary of all the scraped tweets and sentiment of each tweet")
    parser.add_argument('--user', required=True, help='The Twitter handle of the twitter user')
    arg = parser.parse_args()
    user = str(arg.user).replace("@", "")
    main(user)

