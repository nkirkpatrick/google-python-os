#!/usr/bin/env python3

user_statistics = {}

user_statistics = {

    'ac': {
        'INFO_CNT': 0,
        'ERROR_CNT': 1,
    },

    'bob': {
        'INFO_CNT': 2,
        'ERROR_CNT': 2,
    },

    'norbert': {
        'INFO_CNT': 10,
        'ERROR_CNT': 0,
    },
}

user_statistics['norbert']['INFO_CNT']+=1
user_statistics['norbert']['ERROR_CNT']+=1

user_statistics['bob']={'INFO_CNT':0,'ERROR_CNT':1}

print(user_statistics)







