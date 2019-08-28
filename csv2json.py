#!/usr/bin/python

import sys
import csv
import json
import os

# main program
records = []
with open(sys.argv[1], "rb") as csvfile:
    parsed_data = csv.reader(csvfile, delimiter=',', quotechar='"')
    for record in parsed_data:
        records.append(record)
csvfile.close()
print "data parsed from file " + sys.argv[1]
filename = os.path.splitext(os.path.basename(sys.argv[1]))[0] + '.json'
jsonfile = open(filename, "wb")
json.dump(records, jsonfile)
jsonfile.close()
print "data dumped to file " + filename
