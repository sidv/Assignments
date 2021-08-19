#!/bin/bash

lines=`cat aids.csv | wc -l`

cat aids.csv | tail -n $((lines-1)) | while read l
do
	year=`echo $l | cut -d "," -f2 | cut -d '"' -f2`
	adults=`echo $l | cut -d "," -f12 | cut -d '"' -f2`
	echo $adults
	if (( $year > 2005 && $adults > 10000 )) 
	then echo $l
	fi
done
