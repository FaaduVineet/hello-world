#!/usr/bin/python2.7

import json
import csv

sourceFile = open("metadata.json", "rU")

json_data = json.load(sourceFile)

outputFile = open("ConvertedJSON.csv", "w")

outputWriter = csv.writer(outputFile)

#print json_data
lat1=[]
#print type(lat1)
#print json_data["Time"]
#print json_data["videoMetaData"]

for videoData in json_data["videoMetaData"]:
    #print type(lat1)
    lats = videoData["lat"]
    lat2 = int(lats)   
    lat1.append(lats)   

    #print lat1
 
    #print lat1
    #for i in range():
    #print lat2
    #print type(lat2)
    #print 'lats========', lats
    #print "lat, long, speed, timestamp:======" , videoData["lat"], videoData["long"], videoData["speed"], videoData["timestamp"]
    #row_array = []
    #row_array.append(json_data["Time"])

print lat1
print len(lat1)
#for i in lat1:
#    if i == 91.0:
#        print "GPS not available!!!"
