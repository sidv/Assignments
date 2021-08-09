#!/bin/bash

cat aids.csv | while read l
do
	year=`echo $l | cut -d"," -f2 | sed 's/"//g'`
	adult=`echo $l | cut -d"," -f12 | sed 's/"//g'`
	if [[ $year -gt 2005 && $adult -gt 10000 ]]
	then
		echo $l
	fi
done
	
