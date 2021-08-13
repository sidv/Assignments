#!/bin/bash


line=`wc -l airlines.csv`
cat airlines.csv| tail -n $(( lines - 1 )) | while read line
do
	month=`echo $line | cut -d"," -f6 | tr -d '""'`
	year=`echo $line | cut -d"," -f7 | tr -d '"'`
	if [[ $month == 'July' ]]
	then
		if [[ $year -gt 2009 ]]
		then
			echo $line >> data.txt
		fi
	fi
done
