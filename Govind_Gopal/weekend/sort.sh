#!/bin/bash

numb=`cat aids.csv | wc -l`
cat aids.csv | tail -n $(( numb - 1 )) | while read line
do
        comp=2007
        year=`echo $line | cut -d"," -f2 | tr -d '"'`
 
        if [[ $year -gt $comp ]]
        then 
                echo $line
        fi
done



