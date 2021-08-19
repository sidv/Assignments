#!/bin/bash

num_lines=`cat aids.csv | wc -l`
cat aids.csv | tail -n $((num_lines -1)) | while read row
do
        year=`echo $row | cut -d "," -f2 | tr -d '"'`
        #echo $year
	if [[ $year -gt 2007 ]]
	then
		echo $row
	fi
	
done
