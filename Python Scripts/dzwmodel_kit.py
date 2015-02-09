#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      dwoo57
#
# Created:     16/01/2015
# Copyright:   (c) dwoo57 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import helper
import csv
import numpy as np
import random
import math
import matplotlib.pylab as plt

from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

tweetsInputFilePath = "C:\\Users\\dwoo57\\Google Drive\\Career\\Projects\\Trending Topics\\Scipts\\Analysis\\Cluster_Trends_0111_to_0125_2_week\\Output_tweets_interval_rates_trending_topics_2015_0111_to_0125_V2.csv"
#tweetsOutputFilePath = "C:\\Users\\dwoo57\\Google Drive\\Career\\Projects\\Trending Topics\\Scipts\\Analysis\\Cluster_Trends_0111_to_0125_2_week\\Cluster_Output_tweets_interval_rates_trending_topics_2015_0111_to_0125_V2.csv"
tweetsclOutputFilePath = "C:\\Users\\dwoo57\\Google Drive\\Career\\Projects\\Trending Topics\\Scipts\\Analysis\\Cluster_Trends_0111_to_0125_2_week\\Cluster_Groups_Output_tweets_interval_rates_trending_topics_2015_0111_to_0125_V2.csv"
#tweetsRowHeaderOutputFilePath = "C:\\Users\\dwoo57\\Google Drive\\Career\\Projects\\Trending Topics\\Scipts\\Analysis\\Cluster_Trends_0111_to_0125_2_week\\Cluster_Groups_Output_tweets_rowheader.csv"
#tweetsRowIndexOutputFilePath = "C:\\Users\\dwoo57\\Google Drive\\Career\\Projects\\Trending Topics\\Scipts\\Analysis\\Cluster_Trends_0111_to_0125_2_week\\Cluster_Groups_Output_tweets_rowindex.csv"
#tweetsColumnHeaderOutputFilePath = "C:\\Users\\dwoo57\\Google Drive\\Career\\Projects\\Trending Topics\\Scipts\\Analysis\\Cluster_Trends_0111_to_0125_2_week\\Cluster_Groups_Output_tweets_columnheader.csv"
#tweetsColumnIndexOutputFilePath = "C:\\Users\\dwoo57\\Google Drive\\Career\\Projects\\Trending Topics\\Scipts\\Analysis\\Cluster_Trends_0111_to_0125_2_week\\Cluster_Groups_Output_tweets_columnindex.csv"

def DTWDistance(s1, s2,w):
    DTW={}

    w = max(w, abs(len(s1)-len(s2)))

    for i in range(-1,len(s1)):
        for j in range(-1,len(s2)):
            DTW[(i, j)] = float('inf')
    DTW[(-1, -1)] = 0

    for i in range(len(s1)):
        for j in range(max(0, i-w), min(len(s2), i+w)):
            dist= (s1[i]-s2[j])**2
            DTW[(i, j)] = dist + min(DTW[(i-1, j)],DTW[(i, j-1)], DTW[(i-1, j-1)])

    return math.sqrt(DTW[len(s1)-1, len(s2)-1])

def LB_Keogh(s1,s2,r):
    LB_sum=0
    for ind,i in enumerate(s1):

        lower_bound=min(s2[(ind-r if ind-r>=0 else 0):(ind+r)])
        upper_bound=max(s2[(ind-r if ind-r>=0 else 0):(ind+r)])

        if i>upper_bound:
            LB_sum=LB_sum+(i-upper_bound)**2
        elif i<lower_bound:
            LB_sum=LB_sum+(i-lower_bound)**2

    return math.sqrt(LB_sum)

def k_means_clust(groups_dtw,data,num_clust,num_iter,w=5):
    centroids=random.sample(data,num_clust)
    counter=0

    groups_topic ={}

    for n in range(num_iter):
        counter+=1
        print counter
        assignments={}
        #assign data points to clusters
        for ind,i in enumerate(data):
            min_dist=float('inf')
            closest_clust=None
            for c_ind,j in enumerate(centroids):
                if LB_Keogh(i,j,5)<min_dist:
                    cur_dist=DTWDistance(i,j,w)
                    if cur_dist<min_dist:
                        min_dist=cur_dist
                        closest_clust=c_ind
            if closest_clust in assignments:
                assignments[closest_clust].append(ind)
            else:
                assignments[closest_clust]=[]

        #recalculate centroids of clusters
        for key in assignments:
            clust_sum=0
            for k in assignments[key]:
                clust_sum=clust_sum+data[k]

                # for last iteration print groups out
                if n == num_iter -1 :
                    if k not in groups_topic:
                        groups_topic[k] = key

            centroids[key]=[m/len(assignments[key]) for m in clust_sum]

        # then need to sort dictionary by topic and print groups out
        for key in sorted(groups_topic.iterkeys(),reverse = False):
            groups_dtw[key] = groups_topic[key]

    return centroids,groups_dtw

#create function to reorder matrix based on column values
def Take2dArrayOrderByColumnHeader(inputarray,columnlabels,rowlabels):

    #outarray = np.zeros((len(rowlabels), len(columnlabels)), dtype = 'f4')
    outarray = np.zeros((len(rowlabels), 121), dtype = 'f4')

    index = 0
    for label in columnlabels:
        print index,label
        if label != 'foo':
            outarray[:,int(float(label))] = inputarray[:,index]
        index +=1

    return outarray

def KMeansClustBasedOnDynamicTimeWrapping(tweetsInputFilePath,num_clust,tweetsclOutputFilePath,tweetsclCentriodsOutputFilePath):
    #data = helper.ImportFileConvertToNumpyArray(tweetsInputFilePath,0,',','a10,f4,f4,f4,f4')
    data = helper.ImportCSVFileConvertToNumpyArray(tweetsInputFilePath)
    data = data[:,[0,1,4]]
    #reader = csv.reader( open(tweetsInputFilePath) )

    # this gets unique rows?
    rows, row_pos = np.unique(data[:, 0], return_inverse=True)
    cols, col_pos = np.unique(data[:, 1], return_inverse=True)
    rows, row_pos = np.unique(data[:, 0], return_inverse=True)
    cols, col_pos = np.unique(data[:, 1], return_inverse=True)

    pivot_table = np.zeros((len(rows), len(cols)), dtype = 'f4')
    #pivot_table = np.zeros((len(rows), len(cols)), dtype=data.dtype)
    pivot_table[row_pos, col_pos] = data[:, 2]
    data_pivoted = pivot_table

    data_pivoted_colsorted = Take2dArrayOrderByColumnHeader(data_pivoted,cols,rows)

    groups_dtw = np.zeros(len(rows), dtype = 'f4')
    centroids,groups_dtw =k_means_clust(groups_dtw,data_pivoted_colsorted,num_clust,4,4)

    score = silhouette_score(data_pivoted_colsorted,groups_dtw)
    print score

    np.savetxt(tweetsclOutputFilePath, groups_dtw)
    np.savetxt(tweetsclCentriodsOutputFilePath, centroids)

    for i in centroids:
        plt.plot(i)

    plt.show()

def LoadTweetsIntervalRatesIntoPivotTable(tweetsInputFilePath):
    #data = helper.ImportFileConvertToNumpyArray(tweetsInputFilePath,0,',','a10,f4,f4,f4,f4')
    data = helper.ImportCSVFileConvertToNumpyArray(tweetsInputFilePath)
    data = data[:,[0,1,4]]
    #reader = csv.reader( open(tweetsInputFilePath) )

    # this gets unique rows?
    rows, row_pos = np.unique(data[:, 0], return_inverse=True)
    cols, col_pos = np.unique(data[:, 1], return_inverse=True)
    rows, row_pos = np.unique(data[:, 0], return_inverse=True)
    cols, col_pos = np.unique(data[:, 1], return_inverse=True)

    pivot_table = np.zeros((len(rows), len(cols)), dtype = 'f4')
    #pivot_table = np.zeros((len(rows), len(cols)), dtype=data.dtype)
    pivot_table[row_pos, col_pos] = data[:, 2]
    data_pivoted = pivot_table

    data_pivoted_colsorted = Take2dArrayOrderByColumnHeader(data_pivoted,cols,rows)

    groups_dtw = np.zeros(len(rows), dtype = 'f4')

    return data_pivoted_colsorted, groups_dtw

#This is different from above. Maybe remain above to fit. This takes the clusters from above and then assigns them
def Predict_k_means_clust(centroids,tweets,groups_dtw,w=5):
    #centroids=random.sample(data,num_clust)
    #counter=0

    groups_topic ={}
    assignments={}

    #1.Import centriods
    #2.Import tweet rate

    #3.Then assign each topics to the nearest centriod
    for ind,i in enumerate(tweets):
            min_dist=float('inf')
            closest_clust=None
            for c_ind,j in enumerate(centroids):
                if LB_Keogh(i,j,5)<min_dist:
                    cur_dist=DTWDistance(i,j,w)
                    if cur_dist<min_dist:
                        min_dist=cur_dist
                        closest_clust=c_ind
            if closest_clust in assignments:
                assignments[closest_clust].append(ind)
            else:
                assignments[closest_clust]=[]

    for key in assignments:
        for k in assignments[key]:
            if k not in groups_topic:
                        groups_topic[k] = key

    #4.Return assignments, for each topic what group do they belong to
    for key in sorted(groups_topic.iterkeys(),reverse = False):
            groups_dtw[key] = groups_topic[key]


    #5. Then plot centroids and their topics
    index = 0
    for i in centroids:

        plt.plot(i)
        plt.show() #show orginal clusters
        for topics in assignments[index]:
            print assignments[index]
            plt.plot(tweets[topics])

        plt.show()
        index +=1

    return groups_dtw


def PredictAssignClosestClusterBasedOnDynamicTW(tweetsclCentriodsOutputFilePath_trend,tweetsclCentriodsOutputFilePath_nontrend, loc_output_TRENDING_tweetrate_TEST):

    #1a Load trending clusters
    #1b Load nontrending clusters
    pivot_table_trending = np.loadtxt(tweetsclCentriodsOutputFilePath_trend)
    pivot_table_nontrending = np.loadtxt(tweetsclCentriodsOutputFilePath_nontrend)

    pivot_table_clusters = np.concatenate((pivot_table_trending, pivot_table_nontrending))

    #2.load data and then Assign topics to closest cluster
    tweets, groups_dtw = LoadTweetsIntervalRatesIntoPivotTable(loc_output_TRENDING_tweetrate_TEST)

    #3.Then return topics and which groups they belong to
    groups_dtw = Predict_k_means_clust(pivot_table_clusters,tweets,groups_dtw)

    return

#if __name__ == '__main__':
#    main()
