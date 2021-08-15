#!/bin/bash

lines=`cat aids.csv | wc -l`

cat aids.csv | tail -n $((lines-1)) | while read l
do
	allages=`echo $l | cut -d "," -f13 | cut -d '"' -f2`
	female=`echo $l | cut -d "," -f15 | cut -d '"' -f2 | cut -d '.' -f1`
	echo $allages
	if (( $allages > 100 && $female <100 )) 
	then echo $l
	fi
done
