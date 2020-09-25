# -*- coding: utf-8 -*-

import tweepy  # https://www.tweepy.org
import csv

consumer_key = 'YOUR CONSUMER KEY'
consumer_secret = 'YOUR CONSUMER SECRET'
access_key = 'YOUR ACCESS KEY'
access_secret = 'YOUR SECRET'


def search_tweets(text_query, number_of_tweets):
    # initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    # initialize a list to hold all the tweets
    all_tweets = []

    # make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.search(q=text_query, count=200, tweet_mode="extended")

    all_tweets.extend(new_tweets)
    while len(new_tweets) > 0:
        if len(all_tweets) >= number_of_tweets - 100:
            break
        new_tweets = api.search(q=text_query, count=200, tweet_mode="extended")
        all_tweets.extend(new_tweets)
        print("...%s tweets extracted so far" % (len(all_tweets)))

    out_tweets = [[tweet.id_str,
                   tweet.created_at,
                   tweet.full_text.encode("utf-8")] for tweet in all_tweets]

    # write the csv file
    with open('%s.csv' % text_query, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['id_str',
                         'created_at',
                         'full_text(utf-8)'])
        writer.writerows(out_tweets)
    pass


if __name__ == '__main__':
    # X is approximate number of tweets to be retrieved.
    search_tweets('YOUR QUERY', X)
