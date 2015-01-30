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
##loc_tweets_list = [
##"C:\\Users\\dwoo57\\Google Drive\\Career\\Projects\\Trending Topics\\Scipts\\Analysis\\Cluster_Trends_0111_to_0119_1week\\Raw_Data\\sample_combined_20150110.csv",
##"C:\\Users\\dwoo57\\Google Drive\\Career\\Projects\\Trending Topics\\Scipts\\Analysis\\Cluster_Trends_0111_to_0119_1week\\Raw_Data\\sample_combined_20150111.csv",
##"C:\\Users\\dwoo57\\Google Drive\\Career\\Projects\\Trending Topics\\Scipts\\Analysis\\Cluster_Trends_0111_to_0119_1week\\Raw_Data\\sample_combined_20150112.csv",
##"C:\\Users\\dwoo57\\Google Drive\\Career\\Projects\\Trending Topics\\Scipts\\Analysis\\Cluster_Trends_0111_to_0119_1week\\Raw_Data\\sample_combined_20150113.csv",
##"C:\\Users\\dwoo57\\Google Drive\\Career\\Projects\\Trending Topics\\Scipts\\Analysis\\Cluster_Trends_0111_to_0119_1week\\Raw_Data\\sample_combined_20150114.csv",
##"C:\\Users\\dwoo57\\Google Drive\\Career\\Projects\\Trending Topics\\Scipts\\Analysis\\Cluster_Trends_0111_to_0119_1week\\Raw_Data\\sample_combined_20150115.csv",
##"C:\\Users\\dwoo57\\Google Drive\\Career\\Projects\\Trending Topics\\Scipts\\Analysis\\Cluster_Trends_0111_to_0119_1week\\Raw_Data\\sample_combined_20150116.csv",
##"C:\\Users\\dwoo57\\Google Drive\\Career\\Projects\\Trending Topics\\Scipts\\Analysis\\Cluster_Trends_0111_to_0119_1week\\Raw_Data\\sample_combined_20150117.csv",
##"C:\\Users\\dwoo57\\Google Drive\\Career\\Projects\\Trending Topics\\Scipts\\Analysis\\Cluster_Trends_0111_to_0119_1week\\Raw_Data\\sample_combined_20150118.csv",
##"C:\\Users\\dwoo57\\Google Drive\\Career\\Projects\\Trending Topics\\Scipts\\Analysis\\Cluster_Trends_0111_to_0119_1week\\Raw_Data\\sample_combined_20150119.csv"]

loc_tweets_list = [
"C:\\Users\\dwoo57\\Documents\\Career_mirror_gdrive\\Projects\\Trending Topics\\Tweets\\sample_combined_20150120.csv",
"C:\\Users\\dwoo57\\Documents\\Career_mirror_gdrive\\Projects\\Trending Topics\\Tweets\\sample_combined_20150121.csv",
"C:\\Users\\dwoo57\\Documents\\Career_mirror_gdrive\\Projects\\Trending Topics\\Tweets\\sample_combined_20150122.csv",
"C:\\Users\\dwoo57\\Documents\\Career_mirror_gdrive\\Projects\\Trending Topics\\Tweets\\sample_combined_20150123.csv",
"C:\\Users\\dwoo57\\Documents\\Career_mirror_gdrive\\Projects\\Trending Topics\\Tweets\\sample_combined_20150124.csv",
"C:\\Users\\dwoo57\\Documents\\Career_mirror_gdrive\\Projects\\Trending Topics\\Tweets\\sample_combined_20150125.csv",
"C:\\Users\\dwoo57\\Documents\\Career_mirror_gdrive\\Projects\\Trending Topics\\Tweets\\sample_combined_20150126.csv"]


loc_trending_topics = "C:\\Users\\dwoo57\\Google Drive\\Career\\Projects\\Trending Topics\\Scipts\\Analysis\\Cluster_Trends_0111_to_0125_2_week\\Raw Data\\trending_topics_2015_0111_to_0125.csv"
loc_all_trending_topics = "C:\\Users\\dwoo57\\Google Drive\\Career\\Projects\\Trending Topics\\Scipts\\Analysis\\Cluster_Trends_0111_to_0125_2_week\\Raw Data\\trending_topics_2015_0111_to_0125_all_ranks.csv"
loc_output_trending_tweets = "C:\\Users\\dwoo57\\Google Drive\\Career\\Projects\\Trending Topics\\Scipts\\Analysis\\Cluster_Trends_0111_to_0125_2_week\\sample_trending_tweets_2015_0111_to_0125_cleaned.csv" # will be created
#loc_output_nontrending_tweets = "C:\\Users\\dwoo57\\Google Drive\\Career\\Projects\\Trending Topics\\Scipts\\Data\\Tweets\\Combined\\nontrending_tweets_20141224_cleaned.csv"
loc_output_remaining_tweets = "C:\\Users\\dwoo57\\Google Drive\\Career\\Projects\\Trending Topics\\Scipts\\Analysis\\Cluster_Trends_0111_to_0125_2_week\\remaining_tweets_2015_0111_to_0125_cleaned.csv"
#C:\Users\dwoo57\Google Drive\Career\Projects\Trending Topics\Scipts\Analysis\Cluster_Trends_0111_to_0125_2_week\Raw Data\trending_topics_2015_0111_to_0125.csv

# Description: This methods takes two files check for matches and then writes matches to a file
def reduce_data(loc_tweets, loc_trending_topics,loc_all_trending_topics, loc_output_trending_tweets,loc_output_remaining_tweets):
    start = datetime.now()
    debug = False
    remaning_files =[]
    trending_tweets=[]

  #get all categories and comps on offer in a dict
    #trending_topics = {}
    trending_topics = []
    all_trending_topics = []
    outofrange_topics = {}

    #step1: Get all trending topics within a certain RANK
    for e, line in enumerate( open(loc_trending_topics) ):
        temp_topic = line.split(",")[0].lower()
        temp_topic = re.sub("[^a-zA-Z0-9]","",temp_topic)
        trending_topics.append(temp_topic)

    #step2: Get ALL trending topics regardless of RANK
    for e, line in enumerate( open(loc_all_trending_topics) ):
        temp_topic = line.split(",")[0].lower()
        temp_topic = re.sub("[^a-zA-Z0-9]","",temp_topic)
        all_trending_topics.append(temp_topic)

    #step3: go through transactions file and reduce
    reduced = 0
    checked = False # this controls if we do the remaining files
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
        cleaned_txt = re.sub("[^a-zA-Z0-9]"," ",txt)
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

            #with open(loc_output_trending_tweets, "ab") as outfile_trending:

            #writer = csv.writer(outfile_trending)

            topic_matched = "\"" + topic_matched + "\"" + "\n"
            line = ",".join((line.rstrip('\n'),topic_matched))

            #writer.writerow([line])
                #outfile_trending.write( '\n'.join(line) )
                #outfile_trending.write("\n")
            #outfile_trending.close()
            trending_tweets.append(line)
            reduced += 1
            checked = True
            continue

        if debug == True:
            print "Finish writing to trend file. Now writing to remaining file"
            print datetime.now() - start

        #This means that the tweets is not part of the RANKED trending topics
        if checked == False:

            #now check if it is in ALL the topics
            output =set(word).intersection(all_trending_topics)

            if len(output) >= 1:
                checked = True

            # this means that is not part of the all trending topics list
            if checked == False:
            #if len(output) == 0:

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

    #write out trending tweets
    f=open(loc_output_trending_tweets, 'a')
    f.writelines("%s" % l for l in trending_tweets)
    f.flush()
    f.close()

    #write out remaining tweets
    f=open(loc_output_remaining_tweets, 'a')
    f.writelines("%s" % l for l in remaning_files)
    f.flush()
    f.close()


if __name__ == '__main__':
    #main()
    counter_file = 0
    for index, val in enumerate(loc_tweets_list):
        print "Processing File Number:  %d" % counter_file
        reduce_data(val, loc_trending_topics, loc_all_trending_topics, loc_output_trending_tweets,loc_output_remaining_tweets)
