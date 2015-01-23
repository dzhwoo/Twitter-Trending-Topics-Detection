# -*- coding: utf-8 -*-
"""
Created on Wed Dec 10 12:47:54 2014

@author: dwoo57
This implements the streamlistener class
"""

from tweepy import StreamListener
import tweepy,json, time, sys,codecs,datetime,csv
from time import gmtime, strftime

tweepy.debug()

class SListener(StreamListener):

    isDebugMode = False

    def __init__(self, api = None, fprefix = 'streamer'):
        self.api = api or API()
        self.counter = 0
        self.fprefix = fprefix
        #self.output  = open(fprefix + '.'
        #                    + time.strftime('%Y%m%d-%H%M%S') + '.json', 'w')
        self.output  = codecs.open(fprefix + '.'
                            + time.strftime('%Y%m%d-%H%M%S') + '.json', 'w',encoding='utf-8')
        self.delout  = open('delete.txt', 'a')

    def on_data(self, data):

        #current_datetime = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        DEBUG = False

        if  'in_reply_to_status' in data:
            if DEBUG == True:
                print "Parsing tweets"

            self.on_status(data)
            #print current_datetime
            #print data

        elif 'delete' in data:

            if DEBUG == True:
                print "Delete status detected"

            delete = json.loads(data)['delete']['status']
            if self.on_delete(delete['id'], delete['user_id']) is False:
                return False
        elif 'limit' in data:

            if DEBUG == True:
                print "Limit status detected"

            if self.on_limit(json.loads(data)['limit']['track']) is False:
                return False
        elif 'warning' in data:

            if DEBUG == True:
                print "Warning status detected"

            warning = json.loads(data)['warnings']
            print (warning['message'])
            return False

    def on_status(self, status):

        DEBUG = False
        #parse tweet into dictionary first for easier indexing
        datadict = json.loads(status)
        #
        try:
            #now save metrics
            id = str(datadict['id_str']).encode('ascii','ignore')
            #text = str(datadict['text']).encode('utf8')
            text = str(datadict['text'].encode('ascii','ignore'))
            text = text.replace('\n','')
            created_at = str(datadict['created_at']).encode('ascii','ignore')

            if datadict['place'] is None:
                country_code ='null'
                place_full_name = 'null'
            else:
                if datadict['place']['country_code'] is None:
                    country_code ='null'
                else:
                    country_code = str(datadict['place']['country_code'].encode('ascii','ignore'))

                if datadict['place']['full_name'] is None:
                    place_full_name = 'null'
                else:
                    place_full_name = str(datadict['place']['full_name'].encode('ascii','ignore'))

            retweet_count = str(datadict['retweet_count']).encode('ascii','ignore')

            if datadict['coordinates'] is None:
                lat = 'null'
                lng = 'null'
            else:
                lat = str(datadict['coordinates']['coordinates'][1]).encode('ascii','ignore')
                lng = str(datadict['coordinates']['coordinates'][0]).encode('ascii','ignore')

            if datadict['user']['location'] is None:
                user_profile_location = 'null'
            else:
                user_profile_location = str(datadict['user']['location'].encode('ascii','ignore'))

            if datadict['user']['time_zone'] is None:
                user_profile_timezone = 'null'
            else:
                user_profile_timezone = str(datadict['user']['time_zone'].encode('ascii','ignore'))

            if DEBUG == True:
                print strftime("%Y-%m-%d %H:%M:%S \n", gmtime())
                print "%s , %s, %s \n" % (text, created_at, country_code)
                print "%s , %s, %s, %s \n" % (place_full_name, retweet_count, lat,lng)


            str_literal = "\""
            #store into list
            #outweet = [id,text,created_at,country_code,place_full_name,retweet_count]
            outweet = str_literal + id + str_literal

            #outweet = outweet.join([",",str_literal, text, str_literal])
            #outweet = outweet.join([",",str_literal, created_at, str_literal])

            outweet +="," + str_literal + text + str_literal
            outweet +="," + str_literal +  created_at + str_literal
            outweet +="," + str_literal + country_code + str_literal
            outweet +="," + str_literal + place_full_name + str_literal
            outweet +="," + str_literal + retweet_count + str_literal
            outweet +="," + str_literal + lat + str_literal
            outweet +="," + str_literal + lng + str_literal
            outweet +="," + str_literal + user_profile_location + str_literal
            outweet +="," + str_literal + user_profile_timezone + str_literal
            outweet= outweet.encode('ascii','ignore')
            #headers = ["id","text","created_at","country_code","place_full_name","retweet_Count"]

            if DEBUG == True:
                print "Completed: combined strings and literals before output file"

            #create heaaders
            if self.counter ==0:
                #self.output.write(headers + "\n")
                self.output.write(outweet + "\n")
            else:
                self.output.write(outweet + "\n")
                #self.output.write(status + "\n") #original code

            # can use below to debug. Show entire tweet.
            #self.output.write(status + "\n")
            self.counter += 1

            if self.counter >= 20000:
            #if self.counter >= 5:
                self.output.close()
                #self.output = open(self.fprefix + '.'
                #                   + time.strftime('%Y%m%d-%H%M%S') + '.json', 'w')
                self.output  = codecs.open(self.fprefix + '.'
                                + time.strftime('%Y%m%d-%H%M%S') + '.json', 'w',encoding='utf-8')
                self.counter = 0

            if DEBUG == True:
                print "Completed: Write tweets to daily file"
        #
        except:
            current_datetime = strftime("%Y-%m-%d %H:%M:%S", gmtime())
            with open('Sample_streaming_tweets_log_file.csv', 'ab') as f:
                writer = csv.writer(f)
                #if num_run == 0 :
                writer.writerow(["error:%s and occured at %s" %(sys.exc_info()[1],current_datetime)])
                writer.writerow(["Attempting to print variables"])
                #writer.writerow([status])
                writer.writerow([id])
                writer.writerow([text])
                writer.writerow([created_at])
                writer.writerow([country_code])
                writer.writerow([place_full_name])
                writer.writerow([retweet_count])
                writer.writerow([lat])
                writer.writerow([lng])
                print str(current_datetime)
                print status
                #writer.writerow([status])
            #pass
            #outweet = "error"
            #outweet = outweet.encode('ascii')

            raise

        return

    def on_delete(self, status_id, user_id):
        self.delout.write( str(status_id) + "\n")
        return

    def on_limit(self, track):
        sys.stderr.write("Limit occured.....\n")
        sys.stderr.write(str(track) + "\n")
        #sys.stderr.write(track + "\n")
        return

    def on_error(self, status_code):
        sys.stderr.write('Error: ' + str(status_code) + "\n")
        return False

    def on_timeout(self):
        sys.stderr.write("Timeout, sleeping for 60 seconds...\n")
        time.sleep(60)
        return