#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:     I think there was duplication when doing trending vs non trending.
#              So,easy win would be to combind the code here. This samples topics
#               from both trending and nontrending, then starts clustering them
#               Does the training as well as the scoring. May use helper methods
#               to organize and more the code more efficient.
#
# Author:      dwoo57
#
# Created:     28/01/2015
# Copyright:   (c) dwoo57 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import helper
import dzwmodel_kit

#TRENDING TOPICS FILES
#topics
loc_input_trending_topics = "C:\\Users\\dwoo57\\Google Drive\\Career\\Projects\\Trending Topics\\Scipts\\Analysis\\Cluster_Trends_0111_to_0125_2_week\\Raw Data\\trending_topics_2015_0111_to_0125.csv"

loc_output_trending_topics_TRAIN_SAMPLED = "C:\\Users\\dwoo57\\Google Drive\\Career\\Projects\\Trending Topics\\Scipts\\Analysis\\Cluster_Trends_0111_to_0125_2_week\\Modeling\\Training\\trending_topics_2015_0111_to_0125_TRAIN_SAMPLED.csv"
loc_output_trending_topics_TEST_SAMPLED = "C:\\Users\\dwoo57\\Google Drive\\Career\\Projects\\Trending Topics\\Scipts\\Analysis\\Cluster_Trends_0111_to_0125_2_week\\Modeling\\Training\\trending_topics_2015_0111_to_0125_TEST_SAMPLED.csv"

#tweets
loc_input_TRENDING_tweetrates = "C:\\Users\\dwoo57\\Google Drive\\Career\\Projects\\Trending Topics\\Scipts\\Analysis\\Cluster_Trends_0111_to_0125_2_week\\Output_tweets_interval_rates_trending_topics_2015_0111_to_0125_V2.csv"
#loc_output_topics = "C:\\Users\\dwoo57\\Google Drive\\Career\\Projects\\Trending Topics\\Scipts\\Analysis\\Cluster_Trends_0111_to_0125_2_week\\test_NONtrending_topics_end_time_SAMPLED.csv"

loc_output_TRENDING_tweetrate_TRAIN = "C:\\Users\\dwoo57\\Google Drive\\Career\\Projects\\Trending Topics\\Scipts\\Analysis\\Cluster_Trends_0111_to_0125_2_week\\Modeling\\Training\\Output_tweets_interval_rates_TRENDING_topics_2015_0111_to_0125_V2_TRAIN_SAMPLED.csv"
loc_output_TRENDING_tweetrate_TEST = "C:\\Users\\dwoo57\\Google Drive\\Career\\Projects\\Trending Topics\\Scipts\\Analysis\\Cluster_Trends_0111_to_0125_2_week\\Modeling\\Training\\Output_tweets_interval_rates_TRENDING_topics_2015_0111_to_0125_V2_TEST_SAMPLED.csv"


# SPLIT

#NONTRENDING TOPICS FILES
loc_input_NON_TRENDING_topics = "C:\\Users\\dwoo57\\Google Drive\\Career\\Projects\\Trending Topics\\Scipts\\Analysis\\Cluster_Trends_0111_to_0125_2_week\\test_NONtrending_topics_end_time_double_quotes_rmv.csv"

loc_output_NON_trending_topics_TRAIN_SAMPLED = "C:\\Users\\dwoo57\\Google Drive\\Career\\Projects\\Trending Topics\\Scipts\\Analysis\\Cluster_Trends_0111_to_0125_2_week\\Modeling\\Training\\NON_trending_topics_2015_0111_to_0125_TRAIN_SAMPLED.csv"
loc_output_NON_trending_topics_TEST_SAMPLED = "C:\\Users\\dwoo57\\Google Drive\\Career\\Projects\\Trending Topics\\Scipts\\Analysis\\Cluster_Trends_0111_to_0125_2_week\\Modeling\\Training\\NON_trending_topics_2015_0111_to_0125_TEST_SAMPLED.csv"

loc_input_NON_TRENDING_tweetrates = "C:\\Users\\dwoo57\\Google Drive\\Career\\Projects\\Trending Topics\\Scipts\\Analysis\\Cluster_Trends_0111_to_0125_2_week\\Output_tweets_interval_rates_NONtrending_topics_2015_0111_to_0125_V2.csv"
#loc_output_topics = "C:\\Users\\dwoo57\\Google Drive\\Career\\Projects\\Trending Topics\\Scipts\\Analysis\\Cluster_Trends_0111_to_0125_2_week\\test_NONtrending_topics_end_time_SAMPLED.csv"
#loc_output_tweetrate = "C:\\Users\\dwoo57\\Google Drive\\Career\\Projects\\Trending Topics\\Scipts\\Analysis\\Cluster_Trends_0111_to_0125_2_week\\Output_tweets_interval_rates_NONtrending_topics_2015_0111_to_0125_V2_SAMPLED.csv"

loc_output_NON_TRENDING_tweetrate_TRAIN = "C:\\Users\\dwoo57\\Google Drive\\Career\\Projects\\Trending Topics\\Scipts\\Analysis\\Cluster_Trends_0111_to_0125_2_week\\Modeling\\Training\\Output_tweets_interval_rates_NON_TRENDING_topics_2015_0111_to_0125_V2_TRAIN_SAMPLED.csv"
loc_output_NON_TRENDING_tweetrate_TEST = "C:\\Users\\dwoo57\\Google Drive\\Career\\Projects\\Trending Topics\\Scipts\\Analysis\\Cluster_Trends_0111_to_0125_2_week\\Modeling\\Training\\Output_tweets_interval_rates_NON_TRENDING_topics_2015_0111_to_0125_V2_TEST_SAMPLED.csv"

#CLUSTER OUTPUT FILES
#TREND_TRAIN_tweetsInputFilePath = "C:\\Users\\dwoo57\\Google Drive\\Career\\Projects\\Trending Topics\\Scipts\\Analysis\\Cluster_Trends_0111_to_0125_2_week\\Modeling\\Training\\Output_tweets_interval_rates_trending_topics_2015_0111_to_0125_V2.csv"
#tweetsOutputFilePath = "C:\\Users\\dwoo57\\Google Drive\\Career\\Projects\\Trending Topics\\Scipts\\Analysis\\Cluster_Trends_0111_to_0125_2_week\\Cluster_Output_tweets_interval_rates_trending_topics_2015_0111_to_0125_V2.csv"
TREND_TRAIN_tweetsclOutputFilePath = "C:\\Users\\dwoo57\\Google Drive\\Career\\Projects\\Trending Topics\\Scipts\\Analysis\\Cluster_Trends_0111_to_0125_2_week\\Modeling\\Training\\Cluster_Groups_Output_tweets_interval_rates_trending_TRAIN_topics_2015_0111_to_0125_V2.csv"
TREND_TRAIN_tweetsCLUSTER_CENTRIODS_OutputFilePath = "C:\\Users\\dwoo57\\Google Drive\\Career\\Projects\\Trending Topics\\Scipts\\Analysis\\Cluster_Trends_0111_to_0125_2_week\\Modeling\\Training\\Cluster_CENTRIODS_Groups_Output_tweets_interval_rates_TRENDING_TRAIN_topics_2015_0111_to_0125_V2.csv"

NONTREND_TRAIN_tweetsclOutputFilePath = "C:\\Users\\dwoo57\\Google Drive\\Career\\Projects\\Trending Topics\\Scipts\\Analysis\\Cluster_Trends_0111_to_0125_2_week\\Modeling\\Training\\Cluster_Groups_Output_tweets_interval_rates_NON_trending_TRAIN_topics_2015_0111_to_0125_V2.csv"
NONTREND_TRAIN_tweetsCLUSTER_CENTRIODS_OutputFilePath = "C:\\Users\\dwoo57\\Google Drive\\Career\\Projects\\Trending Topics\\Scipts\\Analysis\\Cluster_Trends_0111_to_0125_2_week\\Modeling\\Training\\Cluster_CENTRIODS_Groups_Output_tweets_interval_rates_NON_TRENDING_TRAIN_topics_2015_0111_to_0125_V2.csv"


def main():
    #1. Sample topics from trending and non trending. Create two partitions, one for training and one for testing (Monday)

    sampled = True

    if sampled == False:
        #TRENDING
        helper.PartitionFileIntoTrainingAndTestSet(loc_input_trending_topics,loc_output_trending_topics_TRAIN_SAMPLED,loc_output_trending_topics_TEST_SAMPLED,2)

        #training
        topics_train = helper.ReadFileIntoListWithSpecialFormat(loc_output_trending_topics_TRAIN_SAMPLED,0)
        sampled_tweet_rates_train = helper.FilterFileBasedOnList(loc_input_TRENDING_tweetrates,0,topics_train,loc_output_TRENDING_tweetrate_TRAIN)
        helper.WriteListToFile(sampled_tweet_rates_train,loc_output_TRENDING_tweetrate_TRAIN)

        #test
        topics_test = helper.ReadFileIntoListWithSpecialFormat(loc_output_trending_topics_TEST_SAMPLED,0)
        sampled_tweet_rates_test = helper.FilterFileBasedOnList(loc_input_TRENDING_tweetrates,0,topics_test,loc_output_TRENDING_tweetrate_TEST)
        helper.WriteListToFile(sampled_tweet_rates_test,loc_output_TRENDING_tweetrate_TEST)

        #SPLIT

        #NON-TRENDING
        #1 Append random seed to file and only get a sample
        helper.PartitionFileIntoTrainingAndTestSet(loc_input_NON_TRENDING_topics,loc_output_NON_trending_topics_TRAIN_SAMPLED,loc_output_NON_trending_topics_TEST_SAMPLED,300)

        #train
        topics_train = helper.ReadFileIntoList(loc_output_NON_trending_topics_TRAIN_SAMPLED,0)
        sampled_tweet_rates_train = helper.FilterFileBasedOnList(loc_input_NON_TRENDING_tweetrates,0,topics_train,loc_output_NON_TRENDING_tweetrate_TRAIN)
        helper.WriteListToFile(sampled_tweet_rates_train,loc_output_NON_TRENDING_tweetrate_TRAIN)

        #test
        topics_test = helper.ReadFileIntoList(loc_output_NON_trending_topics_TEST_SAMPLED,0)
        sampled_tweet_rates_test = helper.FilterFileBasedOnList(loc_input_NON_TRENDING_tweetrates,0,topics_test,loc_output_NON_TRENDING_tweetrate_TEST)
        helper.WriteListToFile(sampled_tweet_rates_test,loc_output_NON_TRENDING_tweetrate_TEST)

    #2. After samples are created, perform clustering on trending and non trending seperately. (Monday)
        #TRENDING - TRAIN
    num_clust = 4
    dzwmodel_kit.KMeansClustBasedOnDynamicTimeWrapping(loc_output_TRENDING_tweetrate_TRAIN,num_clust,TREND_TRAIN_tweetsclOutputFilePath,TREND_TRAIN_tweetsCLUSTER_CENTRIODS_OutputFilePath)

    num_clust = 4
    dzwmodel_kit.KMeansClustBasedOnDynamicTimeWrapping(loc_output_NON_TRENDING_tweetrate_TRAIN,num_clust,NONTREND_TRAIN_tweetsclOutputFilePath,NONTREND_TRAIN_tweetsCLUSTER_CENTRIODS_OutputFilePath)

    #3. Based on clusters, score each test topic against the clusters and then pick the clusters with the minimum distance (Monday)

    #4. Then score the # of topics correctly identified and # not correctly identify. Use classification metrics

    #5. Then develop parameter to determine prebuffer for interval rates. i.e 10 min from topics and before and use same classification metrics to determine rates


if __name__ == '__main__':
    main()
