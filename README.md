# Description

The goal of this project is to analyze sentiment for a user's tweets.  Their overall persona on Twitter and if its overall positive/negative.  Currently only TextBlob sentiment analyzer is being utilize (NLTK library).  More to be used for better contrast and comparison.  

## Dependencies

- TextBlob
- Vader
- Numpy
- Pandas
- BeautifulSoup

## Usage

The `scrapper.py` python file will be scrapping the Twitter Page to retrieve the tweets.  This does not work on locked or private accounts.  This will not grab all the tweets. It is possible to simulate that through Selenium. The `sentiment_calculator.py` have method that will calculate the sentiment of the tweets provided to them.       
