#!/usr/bin/env python3

# changeJane.py - takes oldFiles.txt as a command line argument and then renames files
# with the new username "jdoe".
 
import sys
import subprocess

print(sys.argv[1])
logfile = sys.argv[1]

#f = open(sys.argv[1], "r")
#for line in f.readlines():
# old_name = line.strip()
# new_name = old_name.replace("jane", "jdoe")
# subprocess.run(["mv", old_name, new_name])
#f.close()

with open(logfile) as f:
    for line in f:
        old_file = line.strip('\n')
        print(old_file)
        new_file = old_file.replace("jane", "jdoe")
        print(new_file)
        print("mv " + old_file + " " + new_file)
        subprocess.run(["mv", old_file, new_file])
f.close()

      
#str = "this is string example....wow!!! this is really string"
#print str.replace("is", "was")
#print str.replace("is", "was", 3)
#        if "CRON" not in line:
#            continue
#        pattern = r"USER \((\w+)\)$"
#        result = re.search(pattern, line)
#        print(result[1])