# -*- coding: utf-8 -*-
"""
Created on Wed Dec 10 12:50:41 2014

@author: dwoo57

Main application to get streaming tweets as well as trending topics every 5mins
"""

from slistener_Vsample import SListener
import time, tweepy, sys, csv,datetime
from time import gmtime, strftime
import traceback

## auth.
## TK: Edit the username and password fields to authenticate from Twitter.
#username = ''
#password = ''
#auth     = tweepy.auth.BasicAuthHandler(username, password)
#api      = tweepy.API(auth)

## Eventually you'll need to use OAuth. Here's the code for it here.
## You can learn more about OAuth here: https://dev.twitter.com/docs/auth/oauth
consumer_key = "8iUevkunn0upi6tXQDo7aQhdY"
consumer_secret = "cvXCF69e4CZGwZdtPK5A8Nw2Q6C69u26DII1N8kaVGv6SBxCjB"
access_key = "2709622146-kVEiNivWIv1Mw7iKME8jRT20p62oOcsZND7UPIN"
access_secret = "O3KSE2iVkyKKKPcN3qsSfMx34eeC3W8h1s7gJS45QkC7p"

# OAuth process, using the keys and tokens

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

def main( mode = 1 ):
    #track  = ['obama', 'egypt']
    #follow = []
    #locations = 23424977 #this is usa

    listen = SListener(api, 'sample')
    stream = tweepy.Stream(auth, listen)

    #print ("Streaming started on %s users and %s keywords..." % (len(track), len(follow)))
    print ("Streaming started...")

    try:
        #stream.filter(track = track, follow = follow)
        #stream.filter()
        #stream.filter(locations=[-125,25,-65,48], async=False)##These coordinates are approximate bounding box around USA
        stream.sample(languages = ['en'])
        #stream.sample()
    except:
        #print ("error:", sys.exc_info()[1])
        current_datetime = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        with open('Sample_streaming_tweets_log_file.csv', 'ab') as f:
            writer = csv.writer(f)
            #if num_run == 0 :
            writer.writerow(["error:%s and occured at %s" %(sys.exc_info()[1],current_datetime)])
            writer.writerow( [traceback.format_exc()])
        stream.disconnect()

if __name__ == '__main__':
    main()
