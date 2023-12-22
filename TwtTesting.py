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

# You can modify the tweet_message variable to tweet different messages or 
# dynamically generate tweets based on various conditions or inputs.
# Explore the Tweepy Documentation for more advanced functionalities like retweeting, liking tweets, following users, searching tweets, etc.