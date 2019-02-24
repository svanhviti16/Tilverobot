from random import choice
import sys, tweepy
from os import environ

# Accepts 3 .txt file parameters
with open(sys.argv[1], encoding="utf-8") as lo_hk, open(sys.argv[2], encoding="utf-8") as no_hk, open(sys.argv[3], encoding="utf-8") as no_ft, open(sys.argv[4], encoding="utf-8") as no_et:
    lo_list = [word.strip() for word in lo_hk]
    no_hk_list = [word.strip() for word in no_hk]
    no_ft_list = [word.strip() for word in no_ft]
    no_et_list = [word.strip() for word in no_et]

def tweet_the_thing(tweet):

    CONSUMER_KEY = environ['CONSUMER_KEY']
    CONSUMER_SECRET = environ['CONSUMER_SECRET']
    ACCESS_KEY = environ['ACCESS_KEY']
    ACCESS_SECRET = environ['ACCESS_SECRET']

    tw_auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    tw_auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    tw_api = tweepy.API(tw_auth)
    tw_api.update_status(tweet)
    print(tweet)

# Outputs random words from the files in a sentence
def getTweet():
    return f'Tilvera okkar er {choice(lo_list)} {choice(no_hk_list)}. Við erum {choice(no_ft_list)} og {choice(no_et_list)} okkar er {choice(no_et_list)}.'

#tweet_the_thing(getTweet())
print(getTweet())