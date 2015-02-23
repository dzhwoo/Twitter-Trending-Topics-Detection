#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      dwoo57
#
# Created:     14/01/2015
# Copyright:   (c) dwoo57 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import helper
import dzwmodel_kit
import numpy as np
import random
import math
import matplotlib.pylab as plt

topicsInputFilePath = "C:\\Users\\dwoo57\\Google Drive\\Career\\Projects\\Trending Topics\\Modeling\\Cluster_Trends_0111_to_0125_2_week\\Raw Data\\trending_topics_2015_0111_to_0125.csv"
topicindex = 0
startdateindex = 1

ListOftweetsInputFilePath = [
"C:\\Users\\dwoo57\\Google Drive\\Career\\Projects\\Trending Topics\\Modeling\\Cluster_Trends_0111_to_0119_1week\\test_trending_tweets_015_0111_to_0119_cleaned_step3_reformat_datetime.csv",
"C:\\Users\\dwoo57\\Google Drive\\Career\\Projects\\Trending Topics\\Modeling\\Cluster_Trends_0111_to_0125_2_week\\1_Clean_Format_Raw_Data\\test_trending_tweets_2015_0120_to_0125_cleaned_step3_reformat_datetime.csv"]


#tweetsInputFilePath = "C:\\Users\\dwoo57\\Google Drive\\Career\\Projects\\Trending Topics\\Scipts\\Analysis\\Cluster_Trends_0111_to_0119_1week\\test_trending_tweets_015_0111_to_0119_cleaned_step3_reformat_datetime.csv"

tweetsOutputFilePath = "C:\\Users\\dwoo57\\Google Drive\\Career\\Projects\\Trending Topics\\Modeling\\Cluster_Trends_0111_to_0125_2_week\\Clusters - 3 clusters 10 iterations with trend smoothing\\Input Files\\Output_tweets_interval_rates_trending_topics_2015_0111_to_0125_V2.csv"

#function ontop because they need to be defined first before main

#2. Then loop through tweets file, for each line, if topic does not exist add, if exist then add count
def IterateTweetsAndCountTweets(tweetsInputFilePath,topics):

        topic_tweet_dict = {'dict1':{'foo':1}}
        rowcount = 0

        #A. First loop through tweet file
        for e, line in enumerate( open(tweetsInputFilePath) ):


            if line == '\n':
                continue
            #B. Split line into fields
            cur_tweet = line.split(",")
            #Bi. Get topic of current line
            cur_line_topic = cur_tweet[len(cur_tweet)-1]
            cur_line_topic = cur_line_topic.strip('\n').strip('/"')
            #Bii. Get min starttime of topic
            topic_trend_start_time = topics[cur_line_topic]



            topics_trend_start_time = helper.ConvertStringToDatetime(topic_trend_start_time,'%m/%d/%Y %H:%M')
            cur_tweet_time = helper.ConvertStringToDatetime(cur_tweet[2],'"%Y-%m-%d %H:%M:%S"')

            #C. For the topic, get min start time from the dictionary
            #D. If tweet is before start time, then go through add to dictionary logics and also check that is within 4 hours

            # note default time delta is days,then deconds
            time_delta = topics_trend_start_time - cur_tweet_time
            time_delta_hours = time_delta.days*24 + (time_delta.seconds + time_delta.microseconds / 1000000.0) / 60.0 /60.0
            time_delta_mins_bin = time_delta_hours*60.0//2.0
            if cur_tweet_time <= topics_trend_start_time:

                # we are normalizing by setting a threshold before detected as trends
                if time_delta_hours <= 4:

                    #if cur_line_topic == "bonnaroo":
                        #x = 1

                    #E. If new topic, create new topic entry
                    if topic_tweet_dict.has_key(cur_line_topic) == True:
                        #Ei then check if the interval exists
                        if topic_tweet_dict[cur_line_topic].has_key(time_delta_mins_bin) == True:
                            topic_tweet_dict[cur_line_topic][time_delta_mins_bin] = topic_tweet_dict[cur_line_topic][time_delta_mins_bin] + 1
                        else:
                             topic_tweet_dict[cur_line_topic][time_delta_mins_bin] = 1
                    else:
                        topic_tweet_dict[cur_line_topic]  = {time_delta_mins_bin:1}
                #F. If new time interval, create new time inter
            #output_dict[tmp_line[keyindex]] = tmp_line[valueindex]
            rowcount = rowcount + 1
            if rowcount % 10000 ==0:
                print rowcount

        return topic_tweet_dict
        #print rowcount

def IterateListOfTweetsAndCountTweets(ListOftweetsInputFilePath,topics):

        topic_tweet_dict = {'dict1':{'foo':1}}
        rowcount = 0

        for index, tweetsInputFilePath in enumerate(ListOftweetsInputFilePath):

            #A. First loop through tweet file
            for e, line in enumerate( open(tweetsInputFilePath) ):


                if line == '\n':
                    continue
                #B. Split line into fields
                cur_tweet = line.split(",")
                #Bi. Get topic of current line
                cur_line_topic = cur_tweet[len(cur_tweet)-1]
                cur_line_topic = cur_line_topic.strip('\n').strip('/"')

                if topics.has_key(cur_line_topic):
                    #Bii. Get min starttime of topic
                    topic_trend_start_time = topics[cur_line_topic]
                else:
                    continue



                topics_trend_start_time = helper.ConvertStringToDatetime(topic_trend_start_time,'%m/%d/%Y %H:%M')
                cur_tweet_time = helper.ConvertStringToDatetime(cur_tweet[2],'"%Y-%m-%d %H:%M:%S"')

                #C. For the topic, get min start time from the dictionary
                #D. If tweet is before start time, then go through add to dictionary logics and also check that is within 4 hours

                # note default time delta is days,then deconds
                time_delta = topics_trend_start_time - cur_tweet_time
                time_delta_hours = time_delta.days*24 + (time_delta.seconds + time_delta.microseconds / 1000000.0) / 60.0 /60.0
                time_delta_mins_bin = time_delta_hours*60.0//2.0
                if cur_tweet_time <= topics_trend_start_time:

                    # we are normalizing by setting a threshold before detected as trends
                    if time_delta_hours <= 4:

                        #if cur_line_topic == "bonnaroo":
                            #x = 1

                        #E. If new topic, create new topic entry
                        if topic_tweet_dict.has_key(cur_line_topic) == True:
                            #Ei then check if the interval exists
                            if topic_tweet_dict[cur_line_topic].has_key(time_delta_mins_bin) == True:
                                topic_tweet_dict[cur_line_topic][time_delta_mins_bin] = topic_tweet_dict[cur_line_topic][time_delta_mins_bin] + 1
                            else:
                                 topic_tweet_dict[cur_line_topic][time_delta_mins_bin] = 1
                        else:
                            topic_tweet_dict[cur_line_topic]  = {time_delta_mins_bin:1}
                    #F. If new time interval, create new time inter
                #output_dict[tmp_line[keyindex]] = tmp_line[valueindex]
                rowcount = rowcount + 1
                if rowcount % 10000 ==0:
                    print rowcount

        return topic_tweet_dict
        #print rowcount

#3. Then create loop to go through dictionary and calculation metrics
def CalculateTweetRatesPerInterval(topic_and_tweets,resultsfile):
    #topic_tweet_dict ={}
    for key, value in topic_and_tweets.iteritems():
        cur_topic = key
        cur_topic_tweets = topic_and_tweets[cur_topic]

        row_count = 0
        str_literal = ','

        # if ascending, t = 0 is when topic was trended.
        for key in sorted(cur_topic_tweets.iterkeys(),reverse = True):

            #print "%s, %s, %s, %s, %s" % (cur_topic, key, cur_topic_tweets[key] , cur_topic_tweets[prev_key] - cur_topic_tweets[key])

            if row_count == 0:
                    tmp_base_tweet_rate = cur_topic_tweets[key]
                    outline = cur_topic + str_literal + str(key)  + str_literal + str(cur_topic_tweets[key]) + str_literal + '0' + str_literal + '0'
            else:
                    #outline = cur_topic + str_literal + str(key)  + str_literal + str(cur_topic_tweets[key]) + str_literal + str(cur_topic_tweets[prev_key] - cur_topic_tweets[key]) + str_literal + str((cur_topic_tweets[prev_key]*1.0 - cur_topic_tweets[key]*1.0)/cur_topic_tweets[prev_key] * 1.0)
                    # now feature is % from base. Base assumes low activity, is it below or above the base. If still trending above, mostly likely trending
                    #outline = cur_topic + str_literal + str(key)  + str_literal + str(cur_topic_tweets[key]) + str_literal + str(cur_topic_tweets[prev_key] - cur_topic_tweets[key]) + str_literal + str((cur_topic_tweets[key]*1.0 - tmp_base_tweet_rate * 1.0 )/tmp_base_tweet_rate * 1.0)

                    #we wanted to smooth the trends lines. the topics are order in descending time period, where each time period leads up to trending topics. Another way to think about it is this a countdown towards being trended
                    curr_rate = (cur_topic_tweets[key]*1.0 - tmp_base_tweet_rate * 1.0 )/tmp_base_tweet_rate * 1.0
                    prev_rate = (cur_topic_tweets[prev_key]*1.0 - tmp_base_tweet_rate * 1.0 )/tmp_base_tweet_rate * 1.0
                    avg_rate = (curr_rate + prev_rate ) /2

                    #outline = cur_topic + str_literal + str(key)  + str_literal + str(cur_topic_tweets[key]) + str_literal + str(cur_topic_tweets[prev_key] - cur_topic_tweets[key]) + str_literal + str((cur_topic_tweets[key]*1.0 - tmp_base_tweet_rate * 1.0 )/tmp_base_tweet_rate * 1.0)
                    outline = cur_topic + str_literal + str(key)  + str_literal + str(cur_topic_tweets[key]) + str_literal + str(avg_rate) + str_literal + str((cur_topic_tweets[key]*1.0 - tmp_base_tweet_rate * 1.0 )/tmp_base_tweet_rate * 1.0)

            f=open(resultsfile, 'a')
            f.write(outline + "\n")
            f.flush()
            f.close()

            row_count = row_count + 1
            prev_key = key

            if row_count % 10000 ==0:
                print row_count

    #topic_and_tweets.

def SampleTopicAndVisualizeTimesSeriesPlot(tweetsInputFilePath,sample_size):
     #data = helper.ImportFileConvertToNumpyArray(tweetsInputFilePath,0,',','a10,f4,f4,f4,f4')
    data = helper.ImportCSVFileConvertToNumpyArray(tweetsInputFilePath)

    # index 3 is with smoothing, 4 is without smoothing
    data = data[:,[0,1,3,4]]
    #reader = csv.reader( open(tweetsInputFilePath) )

    # this gets unique rows?
    rows, row_pos = np.unique(data[:, 0], return_inverse=True)
    cols, col_pos = np.unique(data[:, 1], return_inverse=True)
    rows, row_pos = np.unique(data[:, 0], return_inverse=True)
    cols, col_pos = np.unique(data[:, 1], return_inverse=True)

    pivot_table = np.zeros((len(rows), len(cols)), dtype = 'f4')
    #pivot_table = np.zeros((len(rows), len(cols)), dtype=data.dtype)
    pivot_table_raw = pivot_table
    pivot_table_raw[row_pos, col_pos] = data[:, 2]
    data_pivoted = pivot_table

    data_pivoted_colsorted = dzwmodel_kit.Take2dArrayOrderByColumnHeader(data_pivoted,cols,rows)

##    if sample_size != 0:
##        data = random.sample(data_pivoted,sample_size)

    for i in range(len(data_pivoted)):
        plt.plot(data_pivoted[i])

        if i ==20:
            break

    plt.show()

    #below is for smoothed
    pivot_table_smooth = pivot_table
    pivot_table_smooth[row_pos, col_pos] = data[:, 3]
    data_pivoted = pivot_table_smooth

    data_pivoted_colsorted = dzwmodel_kit.Take2dArrayOrderByColumnHeader(data_pivoted,cols,rows)

##    if sample_size != 0:
##        data = random.sample(data_pivoted,sample_size)

    for i in range(len(data_pivoted)):
        plt.plot(data_pivoted[i])

        if i ==20:
            break

    plt.show()

def main():
    #1. Create loop to iterate through file and get min start time and topic and store this in a dictionary (key is topic and value is start time)
    topics = helper.TakeFileConvertIntoDictionary(topicsInputFilePath,topicindex,startdateindex)
    #topic_and_tweets = IterateTweetsAndCountTweets(tweetsInputFilePath,topics)
    topic_and_tweets = IterateListOfTweetsAndCountTweets(ListOftweetsInputFilePath,topics)
    CalculateTweetRatesPerInterval(topic_and_tweets,tweetsOutputFilePath)

    #next add visualization. This is new after each change. View the results to see how it looks.
    sample_size = 20
    SampleTopicAndVisualizeTimesSeriesPlot(tweetsOutputFilePath,sample_size)
if __name__ == '__main__':
    main()


    #Helper.TakeFileConvertIntoDictionary('test',1,2)



