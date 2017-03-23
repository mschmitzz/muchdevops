#!/usr/bin/python

import random
import time
from twython import Twython, TwythonError

APP_KEY = 'get_your_own_key'
APP_SECRET = 'get_your_own_secret'
OAUTH_TOKEN = 'get_your_own_token'
OAUTH_TOKEN_SECRET = 'get_your_own_secret_token'
twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
WORD_SCRAMBLE = [line.strip() for line in open('words.txt')]
BUZZ_WORDS = [line.strip() for line in open('buzzwords.txt')]
END_WORDS = [line.strip() for line in open('endwords.txt')]
tweet = random.choice(WORD_SCRAMBLE) + ' ' + random.choice(BUZZ_WORDS) + ' ' + random.choice(WORD_SCRAMBLE) + ' ' + random.choice(END_WORDS)
twitter.update_status(status=tweet)
#print tweet
