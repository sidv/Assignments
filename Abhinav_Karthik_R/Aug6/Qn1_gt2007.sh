#!/bin/bash

cat aids.csv | while read l
do
	year=`echo $l | cut -d"," -f2 | sed 's/"//g'`
	if [[ $year -gt 2007 ]]
	then
		echo $l
	fi
done
