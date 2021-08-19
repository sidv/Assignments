#!/bin/bash

lines=`cat aids.csv | wc -l`

cat aids.csv | tail -n $((lines-1)) | while read l
do
	total=`echo $l | cut -d "," -f22 | cut -d '"' -f2`
	
	echo $total
	if (( $total > 100000 )) 
	then 
	country=`echo $l | cut -d "," -f1 | cut -d '"' -f2`
		echo $country
	fi
done
