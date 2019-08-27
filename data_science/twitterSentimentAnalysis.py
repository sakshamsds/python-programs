## Lexicon Based Approach

import tweepy
from textblob import TextBlob  

#API Keys required for supporting the usage of the Twitter APIs
#Access and Consumer keys and secret for authenticating this script to work with the Twitter API
consumer_key = 'OsWJ2Bf0s65vj9xszCDpmORgg'
consumer_secret = 'tzJpKLNZKL7MaT7cRwYNCUn80Pi4SDewzzpFlXw1zlgis7d9XO'
access_token = '898065972501688320-QSCCDaHVSTPyAD96T4HnO3vOi1DfPfW'
access_token_secret = 'Vs1nMADM9wRLZWB6aRoHKFGLxedxjE5Yv4kwpBgwUQUVR'

#Authenticating with Twitter for using its API provided he above keys
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

#API variable for communicating our actions to the Twitter APIs
api = tweepy.API(auth)

#Storing tweets containing the given word
public_tweets = api.search('Trump')

#Analyizing each tweet and outputting the sentiment
for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)
