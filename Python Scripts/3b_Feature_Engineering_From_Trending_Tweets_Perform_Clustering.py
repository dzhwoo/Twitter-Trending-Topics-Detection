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

from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

tweetsInputFilePath = "C:\\Users\\dwoo57\\Google Drive\\Career\\Projects\\Trending Topics\\Scipts\\Analysis\\Cluster_Trends_0111_to_0119_1week\\Output_tweets_interval_rates_trending_topics_2015_0111_to_0119_V2.csv"
tweetsOutputFilePath = "C:\\Users\\dwoo57\\Google Drive\\Career\\Projects\\Trending Topics\\Scipts\\Analysis\\Cluster_Trends_0111_to_0119_1week\\Cluster_Output_tweets_interval_rates_trending_topics_2015_0111_to_0119_V2.csv"
tweetsclOutputFilePath = "C:\\Users\\dwoo57\\Google Drive\\Career\\Projects\\Trending Topics\\Scipts\\Analysis\\Cluster_Trends_0111_to_0119_1week\\Cluster_Groups_Output_tweets_interval_rates_trending_topics_2015_0111_to_0119_V2.csv"
tweetsRowHeaderOutputFilePath = "C:\\Users\\dwoo57\\Google Drive\\Career\\Projects\\Trending Topics\\Scipts\\Analysis\\Cluster_Trends_0111_to_0119_1week\\Cluster_Groups_Output_tweets_rowheader.csv"
tweetsRowIndexOutputFilePath = "C:\\Users\\dwoo57\\Google Drive\\Career\\Projects\\Trending Topics\\Scipts\\Analysis\\Cluster_Trends_0111_to_0119_1week\\Cluster_Groups_Output_tweets_rowindex.csv"
tweetsColumnHeaderOutputFilePath = "C:\\Users\\dwoo57\\Google Drive\\Career\\Projects\\Trending Topics\\Scipts\\Analysis\\Cluster_Trends_0111_to_0119_1week\\Cluster_Groups_Output_tweets_columnheader.csv"
tweetsColumnIndexOutputFilePath = "C:\\Users\\dwoo57\\Google Drive\\Career\\Projects\\Trending Topics\\Scipts\\Analysis\\Cluster_Trends_0111_to_0119_1week\\Cluster_Groups_Output_tweets_columnindex.csv"

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

    outarray = np.zeros((len(rowlabels), len(columnlabels)), dtype = 'f4')

    index = 0
    for label in columnlabels:
        print index,label
        index +=1



def main():
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

    Take2dArrayOrderByColumnHeader(data_pivoted,cols,rows)

    #clustering algorithm
    cluster = KMeans(n_clusters = 4, init = 'k-means++')
    groups = cluster.fit_predict(data_pivoted)

    #implemented performing metrics
    score = silhouette_score(data_pivoted,groups)
    print score
    #l = list(reader)
    #a = np.array(l)

    # quick hack for visualizing. There should be other ways as well
    np.savetxt(tweetsOutputFilePath, data_pivoted)
    np.savetxt(tweetsclOutputFilePath, groups)

    #rows.tofile(fid = tweetsRowHeaderOutputFilePath,sep = ",",format="%s")
    np.savetxt(tweetsRowHeaderOutputFilePath, rows,fmt = '%s')
    np.savetxt(tweetsRowIndexOutputFilePath, row_pos)
    np.savetxt(tweetsColumnHeaderOutputFilePath, cols,fmt = '%s')
    np.savetxt(tweetsColumnIndexOutputFilePath, col_pos)

    #test = a[:,[0,1,4]]
    pass
    #1 import data from file into numpy array
    #2 then perform k means clustering
    #3 then determine performance matrix of clusters
    #4 also visualize results

    groups_dtw = np.zeros(len(rows), dtype = 'f4')
    centroids,groups_dtw =k_means_clust(groups_dtw,data_pivoted,4,4,4)
    #centroids=k_means_clust(data_pivoted,4,10,4)

    score = silhouette_score(data_pivoted,groups_dtw)
    print score
    np.savetxt(tweetsclOutputFilePath, groups_dtw)



if __name__ == '__main__':
    main()
