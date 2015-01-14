#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:      Store all helpers method here that we can reuse over time
#
# Author:      dwoo57
#
# Created:     14/01/2015
# Copyright:   (c) dwoo57 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import re
from datetime import datetime

def TakeFileConvertIntoDictionary(inputfile,keyindex,valueindex):

    output_dict={}
    for e, line in enumerate( open(inputfile) ):
        tmp_line = line.split(",")
        temp_topic = re.sub("[^a-zA-Z]","",tmp_line[keyindex])
        temp_topic = temp_topic.lower()
        output_dict[temp_topic] = tmp_line[valueindex]

    return output_dict

    print "Hello World"


def ConvertStringToDatetime(date_str,date_format):
    #return datetime.strptime(date_str, '%a %b %d %H:%M:%S +0000 %Y')
    return datetime.strptime(date_str, date_format)