#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      dwoo57
#
# Created:     07/01/2015
# Copyright:   (c) dwoo57 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import csv,time

def main():
    pass

# method that takes parameters : file, string to replace, what to replace with
def openfileandfindreplacechar(infilepath,outfilepath,findstr,replacestr):
    #s=open(infilepath).read()
    file = open(infilepath)
    s=file.read()
    if findstr in s:
                print 'Changing "{findstr}" to "{replacestr}"'.format(**locals())
                s=s.replace(findstr, replacestr)
                f=open(outfilepath, 'w')
                f.write(s)
                f.flush()
                f.close()
    else:
                print 'No occurances of "{findstr}" found.'.format(**locals())

# method that reads line of each file and reformats a field into the desired format
#def openfileandfindreformatfield(infilepath,index,curformat,desiredformat):
def openfileandfindreformatfield(infilepath,outfilepath,index):

    error_count =0
    counter = 1
    tweet_list =[]
    #with open(infilepath, "r") as infilepathlines:
        #for line in  csv.reader(infilepathlines, quotechar='"', delimiter=',',
                         #quoting=csv.QUOTE_ALL, skipinitialspace=True):
    for e, line in enumerate( open(infilepath) ):


            try:
                #line.split(",")[2]
                #ts = time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(tweet['created_at'],'%a %b %d %H:%M:%S +0000 %Y')
                line = line.split(",")
                temp_str = line[index]
                #desired_str = time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(line[index],'%a %b %d %H:%M:%S +0000 %Y'))
                desired_str = time.strftime('"%Y-%m-%d %H:%M:%S"', time.strptime(line[index],'"%a %b %d %H:%M:%S +0000 %Y"'))
            except:
                error_count +=1
                continue


            #line = line.replace(temp_str,desired_str)
            line[index] = desired_str
            #str_literal = "\""
            str_literal =""

            list_index = 0
            outline =""
            for w in line:

                if list_index == 0:
                    outline = str_literal + line[list_index] + str_literal
                else:
                    outline += "," + str_literal + line[list_index] + str_literal
                #outline = outline + str_literal + line[1] + str_literal
                #outline = outline + str_literal + line[2] + str_literal
                #outline = outline + str_literal + line[3] + str_literal
                #outline = outline + str_literal + line[1] + str_literal
                #outline = outline + str_literal + line[1] + str_literal
                #outline = outline + str_literal + line[1] + str_literal
                #outline = ",".join((line))
                list_index +=1

            #f=open(outfilepath, 'a')
            #f.write(outline + "\n")
            #f.flush()
            #f.close()

            tweet_list.append(outline)

            if len(tweet_list)>1000000:
                f=open(outfilepath, 'a')
                #f.writelines("%s\n" % l for l in tweet_list)
                f.writelines("%s" % l for l in tweet_list)
                #f.write(outline + "\n")
                f.flush()
                f.close()
                tweet_list = []

                print counter
                counter +=1

    f=open(outfilepath, 'a')
    #f.writelines("%s\n" % l for l in tweet_list)
    f.writelines("%s" % l for l in tweet_list)
    #f.write(outline + "\n")
    f.flush()
    f.close()

    print error_count

if __name__ == '__main__':
    #main()
    infilepath = "C:\\Users\\dwoo57\\Google Drive\\Career\\Projects\\Trending Topics\\Scipts\\Analysis\\Cluster_Trends_0111_to_0119_1week\\sample_trending_tweets_2015_0111_to_0119_cleaned.csv"
    outfilepath = "C:\\Users\\dwoo57\\Google Drive\\Career\\Projects\\Trending Topics\\Scipts\\Analysis\\Cluster_Trends_0111_to_0119_1week\\test_trending_tweets_015_0111_to_0119_cleaned_step1_remove_triple_quotes.csv"
    findstr = '"""'
    replacestr = '""'
    #openfileandfindreplacechar(infilepath,outfilepath,findstr,replacestr)

    infilepath = "C:\\Users\\dwoo57\\Google Drive\\Career\\Projects\\Trending Topics\\Scipts\\Analysis\\Cluster_Trends_0111_to_0119_1week\\test_trending_tweets_015_0111_to_0119_cleaned_step1_remove_triple_quotes.csv"
    outfilepath = "C:\\Users\\dwoo57\\Google Drive\\Career\\Projects\\Trending Topics\\Scipts\\Analysis\\Cluster_Trends_0111_to_0119_1week\\test_trending_tweets_015_0111_to_0119_cleaned_step2_remove_double_quotes.csv"
    findstr = '""'
    replacestr = '"'
    #openfileandfindreplacechar(infilepath,outfilepath,findstr,replacestr)

    infilepath = "C:\\Users\\dwoo57\\Google Drive\\Career\\Projects\\Trending Topics\\Scipts\\Analysis\\Cluster_Trends_0111_to_0125_2_week\\remaining_tweets_2015_0111_to_0125_cleaned.csv"
    outfilepath = "C:\\Users\\dwoo57\\Google Drive\\Career\\Projects\\Trending Topics\\Scipts\\Analysis\\Cluster_Trends_0111_to_0125_2_week\\test_NONtrending_tweets_2015_0120_to_0125_cleaned_step3_reformat_datetime.csv"

    index = 2
    openfileandfindreformatfield(infilepath,outfilepath,index)



