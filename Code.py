import tweepy
from transformers import pipeline


# API keys and access tokens
consumer_key = 'your_consumer_key'
consumer_secret = 'your_consumer_secret'
access_token = 'your_access_token'
access_token_secret = 'your_access_token_secret'

# Authenticate with the Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create the API object
api = tweepy.API(auth)

# Search for tweets
tweets = api.search(q='query', count=100)

# Load the sentiment analysis pipeline
classifier = pipeline('text-classification', model='cardiffnlp/twitter-roberta-base-emotion')

# Analyze the sentiment of each tweet
for tweet in tweets:
    text = tweet.text
    sentiment = classifier(text)[0]['label']
    print(text, sentiment)
