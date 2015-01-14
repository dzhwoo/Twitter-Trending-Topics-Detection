#!/usr/bin/env python
# encoding: utf-8

import tweepy #https://github.com/tweepy/tweepy
import csv
import datetime
from time import gmtime, strftime
import time

#Twitter API credentials
consumer_key = "8iUevkunn0upi6tXQDo7aQhdY"
consumer_secret = "cvXCF69e4CZGwZdtPK5A8Nw2Q6C69u26DII1N8kaVGv6SBxCjB"
access_key = "2709622146-kVEiNivWIv1Mw7iKME8jRT20p62oOcsZND7UPIN"
access_secret = "O3KSE2iVkyKKKPcN3qsSfMx34eeC3W8h1s7gJS45QkC7p"


def get_all_tweets(screen_name,num_run):
	#Twitter only allows access to a users most recent 3240 tweets with this method

    #authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    #initialize a list to hold all the tweepy Tweets
    alltweets = []
    new_tweets = api.trends_place(23424977)

    # 1 is for global
    # 23424977 is for united states

    alltweets.extend(new_tweets)

		#update the id of the oldest tweet less one
	#	oldest = alltweets[-1].id - 1

	#	print "...%s tweets downloaded so far" % (len(alltweets))

	#transform the tweepy tweets into a 2D array that will populate the csv
    #outtweets = [[trend.name, tweet.promoted,tweet.query, tweet.url,tweet.text.encode("utf-8")] for tweet in alltweets]
    current_datetime = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    current_datetime_Str = strftime("%Y%m%d_%H%M",gmtime())
    current_date = strftime("%Y%m%d",gmtime())
    file_name = screen_name + "_" + current_datetime_Str
    file_name = screen_name

    trends = alltweets[0]['trends'];
    outtweets = []
    rank = 1
    #outtweets = [[trend.name, tweet.promoted,tweet.query, tweet.url,tweet.text.encode("utf-8")] for trend in trends]
    for trend in trends:
        outtweets.append([rank,trend['name'].encode("utf-8"),current_datetime])
        rank +=1
        #outtweets = [[trend['name'].encode("utf-8"),current_datetime] for trend in trends]
    # need to encode vs decode from unicode to bytes
    #http://stackoverflow.com/questions/1524262/why-do-i-get-encoding-error-in-python-warnings-formatwarning-on-format-string



	#write the csv
    with open('%s_trending_topics%s_v2_wrank.csv' % (file_name, current_date), 'ab') as f:
        writer = csv.writer(f)
        #if num_run == 0 :
        writer.writerow(['rank','name','current time'])
        writer.writerows(outtweets)
        #elif num_run >=0:
            #writer.writerows(outtweets)
    pass

if __name__ == '__main__':
	#pass in the username of the account you want to download
    is_run = True
    num_run = 0
    num_sleep_sec = 300

    #while num_run < 3:
    while is_run:
        get_all_tweets("usa",num_run)
        num_run +=1
        print num_run
        time.sleep(num_sleep_sec) #wait for 5 mins
