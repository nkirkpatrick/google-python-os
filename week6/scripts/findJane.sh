#!/bin/bash

> oldFiles.txt

for files in $(grep " jane " ../data/list.txt | cut -d ' ' -f 3); do
  echo $files
  if test -e $HOME$files;
     then echo $HOME$files >> oldFiles.txt;
  fi
done
