"""
This file contains the script that accepts tweets from the twitter political dataset at:
https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/PDI7IN
and generates a data matrix (and word index matrix) as input to the GuidedNMF model.

To use this script, first downloaded the tweets from this data set using a hydrator
(we used Twarc). We use tweets from the two files:
democratic-candidate-timelines.txt
republican-candidate-timelines.txt
and combine all tweets into the file "tweets.txt" (inside the data folder).

We note that access to this data requires access to a Twitter Developer account.
To apply for access, refer to: https://developer.twitter.com/apply-for-access.
"""

import json
import os
import numpy as np
import math
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.decomposition import NMF
import nltk
from nltk.corpus import stopwords

FILE = "data/tweets.txt"
months = {'Jan':0, 'Feb':1, 'Mar':2, 'Apr':3, 'May':4, 'Jun':5, 'Jul':6, 'Aug':7, 'Sep':8, 'Oct':9, 'Nov':10, 'Dec':11}

tweets = []
times = []

with open(FILE, "r") as fd:
    while(True):
        line = fd.readline();
        if not line:
            break

        tweet_info = json.loads(line)
        name = tweet_info['user']['name']
        time = tweet_info['created_at'].split(' ')

        month = months[time[1]]
        day = int(time[2])
        year = int(time[5])


        # create a single integer time stamp
        time_stamp = year * 10000 + month * 100 + day

        # For size reasons, we only use tweets after the year 2015 
        # (these should also be the most relevent)

        if(year > 2015):

            text = tweet_info['full_text'].replace("\n", "").replace("\"", "").replace("\r", "")
            text = " ".join([word for word in text.split(" ") if not "http" in word])

            tweets.append(text)
            times.append(time_stamp)

tweets = np.asarray(tweets)
times = np.asarray(times)

#sort the tweets by time
order = np.argsort(times)

tweets = tweets[order]
times = times[order]


stopwords_list = stopwords.words('english')
stopwords_list = stopwords_list + ["rt", "amp"]

# We apply Tfidf to the data matrix
vectorizer = TfidfVectorizer(stop_words = stopwords_list)
vectors = vectorizer.fit_transform(tweets)

idx_to_word = np.array(vectorizer.get_feature_names())

np.save("data/all_tweets.npy", vectors)
np.save("data/all_tweets_words.npy", idx_to_word)

