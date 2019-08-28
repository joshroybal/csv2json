#!/usr/bin/python

import sys
import csv
import json
import os

# main program
jsonfile = open(sys.argv[1], "rb")
records = json.load(jsonfile)
jsonfile.close()
print "data read from file " + sys.argv[1]
filename = os.path.splitext(os.path.basename(sys.argv[1]))[0] + '.csv'
with open(filename, "wb") as csvfile:
    csvwriter = csv.writer(csvfile)
    for record in records:
        csvwriter.writerow(record)
csvfile.close()
print "data written to file " + filename
