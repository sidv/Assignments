#!/bin/bash


cat cars.csv | while IFS=, read l
do
	
	a=`echo $l | cut -d"," -f2 | sed 's/"//g'`
	if [[ $a -gt 200 ]]
	then
		echo $l
	fi

done

