#!/bin/bash
num_lines=`cat aids.csv | wc -l`
cat aids.csv | tail -n $((num_lines -1)) | while read row
do
        country=`echo $row | cut -d "," -f1 | tr -d '"'`
        total_count=`echo $row | cut -d "," -f22 | tr -d '"'`
        #echo $total_count
        if [[ $total_count -gt 100000 ]]
        then
        	echo $country         
        fi

done
