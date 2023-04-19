import tweepy

# Replace with your own keys and tokens
consumer_key = 'your_consumer_key'
consumer_secret = 'your_consumer_secret'
access_token = 'your_access_token'
access_token_secret = 'your_access_token_secret'

# Authenticate to Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create API object
api = tweepy.API(auth)

# Tweet a message
tweet_message = "Hello, this is my first tweet using a Twitter bot!"
api.update_status(tweet_message)

# To be improved
# with More features