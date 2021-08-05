
#! /bin/bash
#read ls
#if [[ -e #ls ]]
#then
#echo 
ls -l  | tr -s " " | cut -d" " -f1,9
#fi
