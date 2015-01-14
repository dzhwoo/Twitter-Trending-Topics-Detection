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

import nltk
from nltk.corpus import stopwords
import sklearn.feature_extraction.text
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import sklearn

loc_input_nontrending_tweets = "C:\\Users\\dwoo57\\Google Drive\\Career\\Projects\\Trending Topics\\Scipts\\Data\\Tweets\\Combined\\remaining_tweets_20141224_cleaned.csv"
loc_ouput_nontrending_tweets = "C:\\Users\\dwoo57\\Google Drive\\Career\\Projects\\Trending Topics\\Scipts\\Data\\Tweets\\Combined\\sampled_remaining_tweets_20141224_cleaned.csv"
#def main():
#    pass

def reduce_data(loc_input_nontrending_tweets,loc_output_nontrending_tweets):
    start = datetime.now()

    #go through transactions file and reduce
    reduced = 0
    checked = False
    index_count = 0
    #open tweets file
    for e, line in enumerate( open(loc_input_nontrending_tweets) ):

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

        if index_count % 101 == 0:
            with open(loc_ouput_nontrending_tweets, "ab") as output:
                writer = csv.writer(output)
                writer.writerow([line])
                #outfile_nontrending.write( '\n'.join(line) )
                #outfile_nontrending.write("\n")
                output.close()
                reduced += 1

        #checked = False
        #print index_count

        #progress, this roughtly equal to every 10min file of tweets
        if index_count % 1000000 == 0:
            print (index_count, reduced, datetime.now() - start)


  #print e, reduced, datetime.now() - start

def createandcountngrams(loc_output_nontrending_tweets):
    start = datetime.now()

    #go through transactions file and reduce
    reduced = 0
    checked = False
    index_count = 0
    cleaned_wordslist = []
    cachedStopWords = stopwords.words("english")

    #1. extract tweet and add to array
    for e, line in enumerate( open(loc_output_nontrending_tweets) ):

        index_count += 1

        if len(line) > 1:
            #print len(line)
            try:
                words = line.split(",")[1]
            except:
                #print txt
                continue
        else:
            continue

        #a use regular expression to search for and remove punctuations
        words = re.sub("[^a-zA-Z]"," ",words)
        #b split setence and convert all to lower case and to individual words
        word = words.lower().split() # use space as delimiter
        #c iterate through the words and remove stop words
        cleaned_words = ' '.join([w for w in word if w not in cachedStopWords])

        #d append back- split text into tokens and then remove stop words. then concatenate back
        cleaned_wordslist.append(cleaned_words)

    #2a tokenize words
    #tokens = nltk.word_tokenize(cleaned_wordslist)

    #2b create bigrams
    vectorizer = CountVectorizer(analyzer ="word", tokenizer = None, preprocessor = None, stop_words = None,max_features = 100,ngram_range =(1,3))
    matrix = vectorizer.fit_transform(cleaned_wordslist)

    freqs = [(word, matrix.getcol(idx).sum()) for word, idx in vectorizer.vocabulary_.items()]
    #sort from largest to smallest
    print (sorted (freqs, key = lambda x: -x[1]))
    
    print ("\n")
    
    # limit words cannot be more than 10% of tweets
    vectorizer = TfidfVectorizer(analyzer ="word", tokenizer = None, preprocessor = None, stop_words = None,max_features = 100,ngram_range =(2,3),max_df=0.1)
    matrix = vectorizer.fit_transform(cleaned_wordslist)

    freqs = [(word, matrix.getcol(idx).sum()) for word, idx in vectorizer.vocabulary_.items()]
    #sort from largest to smallest
    print (sorted (freqs, key = lambda x: -x[1]))

    #bgs = nltk.bigrams(tokens)

    #3 compute frequency
    #fdist = nltk.FreqDist(bgs)
    #fdist.most_common(20)

if __name__ == '__main__':
    #main()
    #reduce_data(loc_input_nontrending_tweets,loc_ouput_nontrending_tweets)
    createandcountngrams(loc_ouput_nontrending_tweets)
