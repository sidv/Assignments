#!/bin/bash

len=`cat aids.csv | wc -l`

cat aids.csv | tail -n $(( len -1 )) | while read line

do

	all=`echo $line | cut -d"," -f22 | tr -d '"'`
	#label=`echo all | cut -d"," -f2`
	if [[ $all -gt 100000  ]]
	then
		echo $line | cut -d"," -f1 | tr -d '"'
	fi

done
