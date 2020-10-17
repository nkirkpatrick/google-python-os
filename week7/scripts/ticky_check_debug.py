#!/usr/bin/env python3

import re
import os
import csv
import operator

# initialize dict variables for error messages and user stats

error_message = {}
user_statistics = {}

# process syslog line and populate error and user dictionaries

def process_syslog(line):
    
    # error_pattern = r'ticky: ERROR ([\w\s\']*) \((.+)\)'
    # info_pattern = r'ticky: INFO.* \((.+)\)'

    if re.search('ticky: ERROR',line):
        print(line)
        # extract error message and insert into error_message dict
        e_msg = re.search(r'ticky: ERROR ([\w\s\']*)', line)
        print("Error Message: " + e_msg.group(1))
        if e_msg.group(1) in error_message:
            error_message[e_msg.group(1)] += 1
        else:
            error_message[e_msg.group(1)] = 1 
        # extract username from error line and update user_statistics dictionary     
        u_name = re.search(r'ticky: ERROR ([\w\s\']*) \((.+)\)', line)
        print("Username: " + u_name.group(2)) 

        if u_name.group(2) in user_statistics:
            user_statistics[u_name.group(2)]['ERROR_CNT']+=1
        else:
            user_statistics[u_name.group(2)]={'INFO_CNT':0,'ERROR_CNT':1}

    elif re.search('ticky: INFO',line):
        print(line)
        # extract username from info line and update user_statistics dictionary
        u_name = re.search(r'ticky: INFO.* \((.+)\)', line)
        print("Info Username: " + u_name.group(1)) 

        if u_name.group(1) in user_statistics:
            user_statistics[u_name.group(1)]['INFO_CNT']+=1
        else:
            user_statistics[u_name.group(1)]={'INFO_CNT':1,'ERROR_CNT':0}

def convert_dict_to_csv():
    
  with open('error_message.csv','w') as f_error:
      writer = csv.writer(f_error)
      writer.writerow(['Error','Count'])
      writer.writerows(error_message_sorted)

  with open('user_statistics.csv','w') as f_stats:
      writer = csv.writer(f_stats)
      writer.writerow(['Username','INFO','ERROR'])
      for username, message_count in user_statistics_sorted:
          row = [username, message_count['INFO_CNT'], message_count['ERROR_CNT']]
          writer.writerow(row)

# read syslog file and process lines

with open('/root/python/week7/scripts/syslog.log','r') as syslog:
    for line in syslog.readlines():
        # print(line)
        process_syslog(line)


# sort error_messages / user_statistics dicts

# print(error_message)
error_message_sorted = sorted(error_message.items(), key = operator.itemgetter(1), reverse = True)
print(error_message_sorted)

# print(user_statistics)
user_statistics_sorted = sorted(user_statistics.items())
print(user_statistics_sorted)

# convert error_message and user_statistic dictionaries to csv
convert_dict_to_csv()













