#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      dwoo57
#
# Created:     30/12/2014
# Copyright:   (c) dwoo57 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from datetime import datetime
import re
import csv

#loc_tweets = "C:\\Users\\dwoo57\\Google Drive\\Career\\Projects\\Trending Topics\\Scipts\\Analysis\\Cluster_Trends_0111_to_0119_1week\\sample_combined_20150113.csv"
loc_tweets_list = [
"C:\\Users\\dwoo57\\Google Drive\\Career\\Projects\\Trending Topics\\Scipts\\Analysis\\Cluster_Trends_0111_to_0119_1week\\Raw_Data\\sample_combined_20150110.csv",
"C:\\Users\\dwoo57\\Google Drive\\Career\\Projects\\Trending Topics\\Scipts\\Analysis\\Cluster_Trends_0111_to_0119_1week\\Raw_Data\\sample_combined_20150111.csv",
"C:\\Users\\dwoo57\\Google Drive\\Career\\Projects\\Trending Topics\\Scipts\\Analysis\\Cluster_Trends_0111_to_0119_1week\\Raw_Data\\sample_combined_20150112.csv",
"C:\\Users\\dwoo57\\Google Drive\\Career\\Projects\\Trending Topics\\Scipts\\Analysis\\Cluster_Trends_0111_to_0119_1week\\Raw_Data\\sample_combined_20150113.csv",
"C:\\Users\\dwoo57\\Google Drive\\Career\\Projects\\Trending Topics\\Scipts\\Analysis\\Cluster_Trends_0111_to_0119_1week\\Raw_Data\\sample_combined_20150114.csv",
"C:\\Users\\dwoo57\\Google Drive\\Career\\Projects\\Trending Topics\\Scipts\\Analysis\\Cluster_Trends_0111_to_0119_1week\\Raw_Data\\sample_combined_20150115.csv",
"C:\\Users\\dwoo57\\Google Drive\\Career\\Projects\\Trending Topics\\Scipts\\Analysis\\Cluster_Trends_0111_to_0119_1week\\Raw_Data\\sample_combined_20150116.csv",
"C:\\Users\\dwoo57\\Google Drive\\Career\\Projects\\Trending Topics\\Scipts\\Analysis\\Cluster_Trends_0111_to_0119_1week\\Raw_Data\\sample_combined_20150117.csv",
"C:\\Users\\dwoo57\\Google Drive\\Career\\Projects\\Trending Topics\\Scipts\\Analysis\\Cluster_Trends_0111_to_0119_1week\\Raw_Data\\sample_combined_20150118.csv",
"C:\\Users\\dwoo57\\Google Drive\\Career\\Projects\\Trending Topics\\Scipts\\Analysis\\Cluster_Trends_0111_to_0119_1week\\Raw_Data\\sample_combined_20150119.csv"]

loc_trending_topics = "C:\\Users\\dwoo57\\Google Drive\\Career\\Projects\\Trending Topics\\Scipts\\Analysis\\Cluster_Trends_0111_to_0119_1week\\Raw_Data\\trending_topics_2015_0111_to_0119.csv"
loc_output_trending_tweets = "C:\\Users\\dwoo57\\Google Drive\\Career\\Projects\\Trending Topics\\Scipts\\Analysis\\Cluster_Trends_0111_to_0119_1week\\sample_trending_tweets_2015_0111_to_0119_cleaned.csv" # will be created
#loc_output_nontrending_tweets = "C:\\Users\\dwoo57\\Google Drive\\Career\\Projects\\Trending Topics\\Scipts\\Data\\Tweets\\Combined\\nontrending_tweets_20141224_cleaned.csv"
#loc_output_remaining_tweets = "C:\\Users\\dwoo57\\Google Drive\\Career\\Projects\\Trending Topics\\Scipts\\Analysis\\0106_0107\\remaining_tweets_20150106_cleaned.csv"

#def main():
#    pass

# methods takes two files check for matches and then writes matches to a file
def reduce_data(loc_tweets, loc_trending_topics, loc_output_trending_tweets):
    start = datetime.now()
    debug = False
    remaning_files =[]

  #get all categories and comps on offer in a dict
    #trending_topics = {}
    trending_topics = []
    outofrange_topics = {}

    for e, line in enumerate( open(loc_trending_topics) ):
        temp_topic = line.split(",")[0].lower()
        temp_topic = re.sub("[^a-zA-Z]","",temp_topic)
        #trending_topics[ line.split(",")[0] ] = 1
        trending_topics.append(temp_topic)
        #trending_topics[ temp_topic ] = 1
    #offers_co[ line.split(",")[3] ] = 1
    #f.close()

    #go through transactions file and reduce
    reduced = 0
    checked = False
    index_count = 0
    #open tweets file
    for e, line in enumerate( open(loc_tweets) ):

        index_count += 1

        if len(line) > 1:
            #print len(line)
            try:
                txt = line.split(",")[1]
            except:
                #print txt
                continue
        else:
            continue

        #1. Remove any puncations or non alphabets
        #2. Tokenize each sentence
        #3. convert to lower case
        #4. Then loop through topics

        if debug == True:
            print "cleaning text"
            print datetime.now() - start
        #a use regular expression to search for and remove punctuations
        cleaned_txt = re.sub("[^a-zA-Z]"," ",txt)
        #b split setence and convert all to lower case and to individual words
        word = cleaned_txt.lower().split() # use space as delimiter
        #c iterate through the words and remove stop words
        #topic_match = [w for w in word if w in trending_topics]

        if debug == True:
            print "cleaning text completed. Now checking for match in topics"
            print datetime.now() - start

        output =set(word).intersection(trending_topics)

        if debug == True:
            print "Topic check complete. Now writing to file"
            print datetime.now() - start

        if len(output) >=1:
            topic_matched = next(iter(output))

            with open(loc_output_trending_tweets, "ab") as outfile_trending:
                #writer = csv.writer(outfile_trending,quoting=csv.QUOTE_MINIMAL,quotechar='')
                #writer = csv.writer(outfile_trending,quoting=csv.QUOTE_NONE,escapechar='',quotechar='')
                #writer = csv.writer(outfile_trending,quotechar='')
                writer = csv.writer(outfile_trending)
                #line = line.rstrip('\n')
                topic_matched = "\"" + topic_matched + "\""
                line = ",".join((line.rstrip('\n'),topic_matched))
                #writer.writerow([line.rstrip('\n'),topic_matched])
                writer.writerow([line])
                    #outfile_trending.write( '\n'.join(line) )
                    #outfile_trending.write("\n")
                outfile_trending.close()
                reduced += 1
                checked = True
                continue

        if debug == True:
            print "Finish writing to trend file. Now writing to remaining file"
            print datetime.now() - start

        if checked == False:

            remaning_files.append(line)

            if len(remaning_files)>= 20000:
                #with open(loc_output_remaining_tweets, "ab") as outfile_remaining:
                    #writer = csv.writer(outfile_remaining)
                    #writer.writerow([line])
                    #outfile_nontrending.write( '\n'.join(line) )
                    #outfile_nontrending.write("\n")
                    #outfile_remaining.close()
                    reduced += 1
        checked = False

        if debug == True:
            print "Finish writing to trend file. Now writing to remaining file"
            print datetime.now() - start

        #progress, this roughtly equal to every 10min file of tweets
        # each file is 20000 rows
        # each day has 100 files
        total_files_per_day = 110
        total_rows_per_file = 20000
        time_to_process_each_file = 2

        if index_count % 20000 == 0:
            estimated_remaning_rows = total_files_per_day * 20000 - index_count
            estimated_time_remaining = estimated_remaning_rows/total_rows_per_file * time_to_process_each_file
            print index_count, reduced, datetime.now() - start
            print estimated_remaning_rows,estimated_time_remaining
  #print e, reduced, datetime.now() - start


if __name__ == '__main__':
    #main()
    counter_file = 0
    for index, val in enumerate(loc_tweets_list):
        print "Processing File Number:  %d" % counter_file
        reduce_data(val, loc_trending_topics, loc_output_trending_tweets)
