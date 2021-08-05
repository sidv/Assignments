#!/bin/bash


cat cars.csv | while IFS=, read l
do
	
	class=`echo $l | cut -d"," -f12 | sed 's/"//g'`
	year=`echo $l | cut -d"," -f16 | sed 's/"//g'`
	if [ "$class" == "Automatic transmission" ]
	then
		if [[ year -gt 2010 ]]
		then
			echo $l
		fi
	fi

done
