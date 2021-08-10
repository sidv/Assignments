#!/bin/bash

cat cancer.csv | while read l
do
	population=`echo $l | cut -d"," -f4 | sed 's/"//g' | cut -d"." -f1`
	rate=`echo $l | cut -d"," -f2 | sed 's/"//g' | cut -d"." -f1`
	if [[ $population -gt 10000000 ]]
	then
		if [[ $rate -gt 200 ]]
		then
			echo $l | cut -d"," -f1
		fi
	fi
done
