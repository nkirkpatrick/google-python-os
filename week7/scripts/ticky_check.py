#!/usr/bin/env python3

import re
import os
import csv
import operator

# initialize dict variables for error messages and user stats

error_messages = {}
user_statistics = {}

# process syslog line and populate error and user dictionaries

def process_syslog(line):
    
    # error_pattern = r'ticky: ERROR ([\w\s\']*) \((.+)\)'
    # info_pattern = r'ticky: INFO.* \((.+)\)'

    if re.search('ticky: ERROR',line):
        print(line)
        # extract error message and insert into dictionary
        y = re.search(r'ticky: ERROR ([\w\s\']*)', line)
        print("Error Message: " + y.group(1))
        if y.group(1) in error_messages:
            error_messages[y.group(1)] += 1
        else:
            error_messages[y.group(1)] = 1      
    

# process syslog file

with open('/Users/norbertkirkpatrick/Documents/Python/Google-Python-OS/week7/scripts/syslog.log','r') as syslog:
    for line in syslog.readlines():
        # print(line)
        process_syslog(line)

print(error_messages)
error_messages_sorted = sorted(error_messages.items(), key = operator.itemgetter(1), reverse = True)
print(error_messages_sorted)









