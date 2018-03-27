import csv

import tweepy
from textblob import TextBlob

# Key and Secret for twitter API
comsumer_key = '[YOUR_VALUE]'
consumer_secret = '[YOUR_VALUE]'

# Access Token and Secret for making API call
access_token = '[YOUR_VALUE]'
access_token_secret = '[YOUR_VALUE]'


def fetch_search_term():
    print("Enter the term to be analyzed...")
    tweet_term = input()

    tweets = fetch_tweets(tweet_term)
    write_tweets_to_file(tweet_term, tweets)


def fetch_tweets(tweet_term):
    # Fetch OAuth instance and tweets from API
    print("Fetching twitter api...")
    auth = tweepy.OAuthHandler(comsumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    tweets = api.search(q=tweet_term, count=100)
    return tweets


def write_tweets_to_file(tweet_term, tweets):
    # Write to file
    file_name = tweet_term + 'tweet_data.csv'
    print("Generating data...")
    with open(file_name, 'w') as file:
        filewriter = csv.writer(file, delimiter=',')
        filewriter.writerow('text,polarity,subjectivity')
        polarity = 0
        for tweet in tweets:
            tweet_blob = TextBlob(tweet.text)
            filewriter.writerow(
                [tweet.text.encode('utf-8'), str(tweet_blob.sentiment.polarity), str(tweet_blob.subjectivity)])
            polarity += tweet_blob.sentiment.polarity

    print("Net polarity is {0}".format(polarity / len(tweets)))
    print("File generated.")


if __name__ == '__main__':
    fetch_search_term()
