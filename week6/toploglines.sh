#!/bin/zsh

for logfile in /var/log/*log; do 
    echo $logfile
    echo "Processing: $logifle"
    cut -d ' ' -f5- $logfile | sort | uniq -c | sort -nr | head -5
done
