#!/bin/bash
cat airlines.csv | while IFS=, read l
do
	month=`echo $l | cut -d"," -f6 | sed 's/"//g'`
	year=`echo $l | cut -d"," -f7 | sed 's/"//g'`
	if [[ "$month" == "July" ]]
	then
		if [[ $year -gt 2009 ]]
		then
			echo $l
		fi
	fi
done < newfile.csv
