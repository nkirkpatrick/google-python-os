import os
import datetime

# file size info
fsize = os.path.getsize("guests.txt")
print(fsize)

# date time info
timestamp = os.path.getmtime("spider_new.txt")
print(timestamp)

fdatetime = datetime.datetime.fromtimestamp(timestamp)
fdate = datetime.date.fromtimestamp(timestamp)
print(fdatetime)
print(fdate)

# file path info
fabspath = os.path.abspath("spider_new.txt")
frelpath = os.path.relpath("spider_new.txt")
print(fabspath)
print(frelpath)
