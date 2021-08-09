#!/bin/bash

count=`cat aids.csv|wc -l`

cat aids.csv|tail -n $((count-1))|while read line
do
	country=`echo $line|tr -s " "|cut -d"," -f1|tr -d '"'`
	total=`echo $line|tr -s " "|cut -d"," -f22|tr -d '"'`

	if (( total > 100000 ))
	then
		echo $country 
	fi
done
