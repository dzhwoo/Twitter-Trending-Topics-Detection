#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      dwoo57
#
# Created:     28/01/2015
# Copyright:   (c) dwoo57 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import helper

loc_input_topics = "C:\\Users\\dwoo57\\Google Drive\\Career\\Projects\\Trending Topics\\Scipts\\Analysis\\Cluster_Trends_0111_to_0119_1week\\test_NONtrending_topics_end_time_double_quotes_rmv.txt"
loc_input_tweets = "C:\\Users\\dwoo57\\Google Drive\\Career\\Projects\\Trending Topics\\Scipts\\Analysis\\Cluster_Trends_0111_to_0119_1week\\Output_tweets_interval_rates_NONtrending_topics_2015_0111_to_0119_V2.csv"

loc_output_topics = "C:\\Users\\dwoo57\\Google Drive\\Career\\Projects\\Trending Topics\\Scipts\\Analysis\\Cluster_Trends_0111_to_0119_1week\\test_NONtrending_topics_end_time_SAMPLED.csv"
loc_output_tweetrate = "C:\\Users\\dwoo57\\Google Drive\\Career\\Projects\\Trending Topics\\Scipts\\Analysis\\Cluster_Trends_0111_to_0119_1week\\Output_tweets_interval_rates_NONtrending_topics_2015_0111_to_0119_V2_SAMPLED.csv"


def main():
    #1 Append random seed to file and only get a sample
    helper.AddRandomNumberToFile(loc_input_topics,loc_output_topics,300)

    #2 Then read interval file and filter based on topics from sample
    topics = helper.ReadFileIntoList(loc_output_topics,0)
    sampled_tweet_rates = helper.FilterFileBasedOnList(loc_input_tweets,0,topics,loc_output_tweetrate)

    #3 Then write out remaning interval file
    helper.WriteListToFile(sampled_tweet_rates,loc_output_tweetrate)
    pass

if __name__ == '__main__':
    main()
