#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      dwoo57
#
# Created:     26/01/2015
# Copyright:   (c) dwoo57 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from datetime import datetime
import re
import csv

loc_input_tweets = "C:\\Users\\dwoo57\\Google Drive\\Career\\Projects\\Trending Topics\\Scipts\\Analysis\\Cluster_Trends_0111_to_0119_1week\\remaining_tweets_2015_0111_to_0119_cleaned.csv"
loc_output_tweets = "C:\\Users\\dwoo57\\Google Drive\\Career\\Projects\\Trending Topics\\Scipts\\Analysis\\Cluster_Trends_0111_to_0119_1week\\remaining_tweets_with_topics.csv"


def OpenFileAppendTopic(inputfile,outputfile):

    output = []
    counter = 1


    for e, line in enumerate( open(inputfile) ):
            temp_text = line.split(",")[1].lower()
            temp_words = temp_text.split(" ")
            topic = "N/A"

            for w in temp_words:
                if "#" in w:
                    topic = w
                    #currently stops are first hashtag, tweets may have multiple topics. chose simple for now.
                    break


            topic = "\"" + topic + "\"" + "\n"
            line = ",".join((line.rstrip('\n'),topic))
            output.append(line)

            if len(output)>1000000:
                f=open(outputfile, 'a')
                #f.writelines("%s\n" % l for l in tweet_list)
                f.writelines("%s" % l for l in output)
                #f.write(outline + "\n")
                f.flush()
                f.close()
                output = []

                print counter
                counter +=1


    print "Completed"

    f=open(outputfile, 'a')
    #f.writelines("%s\n" % l for l in tweet_list)
    f.writelines("%s" % l for l in output)
    #f.write(outline + "\n")
    f.flush()
    f.close()

def main():
    OpenFileAppendTopic(loc_input_tweets,loc_output_tweets)
    #1. Take csv and json file and then iterate through file and search for topic and add to end
    #2 Then write out to results file
    pass

if __name__ == '__main__':
    main()
