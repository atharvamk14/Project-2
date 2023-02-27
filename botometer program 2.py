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

# Enter the list of usernames to be checked
usernames = ['user1', 'user2', 'user3']

# Check the bot scores for all the given usernames
results = bom.check_accounts_in(usernames)

# Print the bot scores for each username
for username, result in results.items():
    print(f'{username}: {result["scores"]["universal"]}')
