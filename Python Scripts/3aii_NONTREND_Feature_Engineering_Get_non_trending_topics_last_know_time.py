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
import helper

loc_input_tweets = "C:\\Users\\dwoo57\\Google Drive\\Career\\Projects\\Trending Topics\\Scipts\\Analysis\\Cluster_Trends_0111_to_0119_1week\\test_NONtrending_tweets_015_0111_to_0119_cleaned_step3_reformat_datetime.csv"
loc_output_tweets = "C:\\Users\\dwoo57\\Google Drive\\Career\\Projects\\Trending Topics\\Scipts\\Analysis\\Cluster_Trends_0111_to_0119_1week\\test_NONtrending_topics_end_time.csv"


def OpenFileAppendTopic(inputfile,outputfile):

    output = []
    counter = 1
    topic_dic = {}
    counter = 1


    for e, line in enumerate( open(inputfile) ):
            temp_text = line.split(",")

            start_time = temp_text[2]
            topic = temp_text[len(temp_text)-1].rstrip('\n')
            if topic == '"N/A"':
                counter +=1
                continue




##            if topic_dic.has_key(topic) == True:
##                cur_topics_convert_start_time = helper.ConvertStringToDatetime(start_time,'"%Y-%m-%d %H:%M:%S"')
##                exist_topics_convert_start_time = helper.ConvertStringToDatetime(topic_dic[topic],'"%Y-%m-%d %H:%M:%S"')
##                if cur_topics_convert_start_time > exist_topics_convert_start_time:
##                    topic_dic[topic] = start_time
##            else:
##                 topic_dic[topic] = start_time

            topic_dic[topic] = start_time

            if counter %100000 == 0:
                print counter

            counter +=1

    print "Completed"

    for key in topic_dic:

        outline = key + "," + topic_dic[key] + "\n"
        #outline = topic + "," + start_time + "/n"

        output.append(outline)

        if len(output)>2000000:
            f=open(outputfile, 'a')
            #f.writelines("%s\n" % l for l in tweet_list)
            f.writelines("%s" % l for l in output)
            #f.write(outline + "\n")
            f.flush()
            f.close()
            output = []

            print counter
            counter +=1


    f=open(outputfile, 'a')
    #f.writelines("%s\n" % l for l in tweet_list)
    f.writelines("%s" % l for l in output)
    #f.write(outline + "\n")
    f.flush()
    f.close()

def main():
    #1.Read in file, get topic and start time from file and dump into csv file
    #2.Then read file and for each topic get the max datetime
    OpenFileAppendTopic(loc_input_tweets,loc_output_tweets)
    pass

if __name__ == '__main__':
    main()
