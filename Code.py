import tweepy
from transformers import pipeline
from prettytable import PrettyTable

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

# Load the sentiment analysis pipeline
classifier = pipeline('text-classification', model='cardiffnlp/twitter-roberta-base-emotion')

# Prompt the user to enter a valid Twitter handle
while True:
    handle = input('Enter a valid Twitter handle (without the @ symbol): ')
    try:
        user = api.get_user(handle)
        break
    except tweepy.TweepError as e:
        print('Error:', e)

# Search for tweets
tweets = api.search_tweets(q=f'from:{handle}', count=100)

# Create a table to display the results
table = PrettyTable()
table.field_names = ['Tweet', 'Sentiment']

# Analyze the sentiment of each tweet and add it to the table
for tweet in tweets:
    text = tweet.text
    sentiment = classifier(text)[0]['label']
    table.add_row([text, sentiment])

# Print the table
print(table)

