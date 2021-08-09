#!/bin/bash

num_lines=`cat cancer.csv | wc -l`
cat cancer.csv | tail -n $((num_lines -1)) | while read row
do
        state=`echo $row | cut -d "," -f1 | tr -d '"'`
        #echo $state
        pop=`echo $row | cut -d "," -f4 | tr -d '"' | tr -d "."`
        pop_r="${pop::-1}"  # remove float value zero
	#echo $pop_r
        total_rate=`echo $row | cut -d "," -f2 | tr -d '"' | tr -d "."`
	total_rate_r="${total_rate::-1}" # remove float value 
        #echo $total_rate
        if  [[ $pop_r -gt 10000000 ]]
 	then
		if [[ $total_rate_r -gt 200 ]]  
		then
			echo $state 
		fi
	fi
done
