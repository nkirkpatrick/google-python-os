import os

# remove examples
if os.path.exists("novel.txt"):
    os.remove("novel.txt")
#os.remove("novel.txt")

# rename examples
if os.path.exists("spider.txt"):
    os.rename("spider.txt", "spider_new.txt")

# validate file exists
print(os.path.exists("spider_new.txt"))
print(os.path.exists("spider.txt"))
