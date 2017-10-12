# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 14:59:21 2017

@author: hp
"""

import nltk 
from nltk.corpus import twitter_samples
from nltk.tag import pos_tag_sents
JJCount=0
NNCount=0
tweets = twitter_samples.strings('positive_tweets.json')
"""Each tweet is stored as a string in a list varibale 'Tweets' """
tweets_token=twitter_samples.tokenized('positive_tweets.json')
"""Each string tweet needs to be broken down to keywords, phrases,symbols etc.
 these are called Tokens """
tweets_tagged = pos_tag_sents(tweets_token)
for tweet in tweets_tagged:
    for pair in tweet:
        if pair[1]=='NN':
         NNCount+=1
        elif pair[1]=='JJ':
         JJCount+=1
print('Total Adjectives= ',JJCount)
print('Total Nouns= ',NNCount)

            
 
 
