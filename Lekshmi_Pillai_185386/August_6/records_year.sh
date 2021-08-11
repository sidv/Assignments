#!/bin/bash

lines=`cat aids.csv | wc -l`

cat aids.csv | tail -n $((lines-1)) | while read l
do
	year=`echo $l | cut -d "," -f2 | cut -d '"' -f2`
	echo $year
	if (( $year > 2007 )) 
	then echo $l
	fi
done
