#!/bin/bash

len=`cat aids.csv | wc -l`

cat aids.csv | tail -n $(( len -1 ))  | while read line

do

	all=`echo $line | cut -d"," -f13 | tr -d '"'`
	if [[ $all -lt 100 ]]
	then
		female=`echo $line | cut -d"," -f15 | tr -d '"'`
		if [[ ${female%.*} -lt 100  ]]
		then
			echo $line
		fi
	fi

done
