#! /bin/bash

lines=`cat aids.csv | wc -l`
cat aids.csv| tail -n $(( lines - 1 )) | while read line
do
        fadults=`echo $line | cut -d"," -f15 | tr -d '"'`
        allages=`echo $line | cut -d"," -f13 | tr -d '"'`
if [[ $allages -lt 100 ]]
#if [[ ${fadults%.*} -lt 100 ]]
then      
	if [[ ${fadults%.*} -lt 100 ]]
	#if [[ $allages -lt 100 ]]
         then
                            echo $line
               fi
       fi

done

