#!/bin/bash


line=`wc -l aids.csv | cut -d" " -f1`

cat aids.csv | tail -n $(( line -1 )) | while read l
do

        year=`echo $l | cut -d"," -f2 | tr -d '"'`
        adults=`echo $l | cut -d"," -f12 | tr -d '"'`
	#echo $adults
        if [[ $year -gt 2005 && $adults -gt 10000 ]]
        then
               echo $l 
        fi
done
