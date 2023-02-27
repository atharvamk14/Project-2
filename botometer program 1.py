import botometer

# API keys and access tokens
rapidapi_key = 'your_rapidapi_key'
twitter_app_auth = {
    'consumer_key': 'your_consumer_key',
    'consumer_secret': 'your_consumer_secret',
    'access_token': 'your_access_token',
    'access_token_secret': 'your_access_token_secret'
}

# Authenticate with the Botometer API
bom = botometer.Botometer(wait_on_ratelimit=True,
                          rapidapi_key=rapidapi_key,
                          **twitter_app_auth)

# Enter the username to be checked
username = input('Enter a Twitter username: ')

# Check the bot score for the given username
result = bom.check_account(username)

# Print the bot score
print('Bot score:', result['scores']['universal'])
