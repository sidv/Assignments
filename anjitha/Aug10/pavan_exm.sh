#!/bin/bash

len=`wc -l covid.csv | cut -d" " -f1`
cat covid.csv | tail -n $((len-1))| while read line
do 

        Death_date=`echo $line | cut -d"," -f5 | tr -d '"'`
#       echo $Death_date
        if [[ Death_date -gt 200 && Death_date -lt 300 ]]
        then
                Countries=`echo $line | cut -d"," -f6 | tr -d '"' >> result.list`
        fi
done 
