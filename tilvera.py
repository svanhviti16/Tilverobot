from random import choice
from credentials import *
import sys, tweepy, requests

# Accepts 3 .txt file parameters
with open(sys.argv[1], encoding="utf-8") as lo_hk, open(sys.argv[2], encoding="utf-8") as no_hk, open(sys.argv[3], encoding="utf-8") as no_kk:
    lo_list = [word.strip() for word in lo_hk]
    no_hk_list = [word.strip() for word in no_hk]
    no_kk_list = [word.strip() for word in no_kk]

def tweet_the_thing(tweet):
    tw_auth = tweepy.OAuthHandler(twitter_consumer_key, twitter_consumer_secret)
    tw_auth.set_access_token(twitter_access_token, twitter_access_token_secret)
    tw_api = tweepy.API(tw_auth)
    tw_api.update_status(tweet)
    print(tweet)

# Outputs random words from the files in a sentence
def getTweet():
    return f'Tilvera okkar er {choice(lo_list)} {choice(no_hk_list)}. Við erum {choice(no_kk_list)} og {choice(no_hk_list)} okkar er {choice(no_hk_list)}.'

tweet_the_thing(getTweet())