#!/bin/bash

lines=`cat cars.csv | wc -l`
cat cancer.csv | tail -n $(( len-1 )) | while read line
do 	
	del=`echo $line | cut -d"," -f4 | tr -d '"'
	if [[ ${del%.*} -gt 10000000 ]]
	then
		c=`echo $line | cut -d"," -f2 | tr -d '"'`
		if [[ ${c%.*} -gt 200 ]]
		then
			echo $line | cut -d"," -f1 | tr -d '"'
		fi
	fi
done
