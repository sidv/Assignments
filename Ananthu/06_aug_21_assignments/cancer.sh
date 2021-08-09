#!/bin/bash

lines=`cat cancer.csv | wc -l`
cat cancer.csv | tail -n $(( $lines - 1 )) | while read line
do
	state=`echo $line | cut -d"," -f1 | tr -d '"'`
	trate=`echo $line | cut -d"," -f2 | tr -d '"'`
	pop=`echo $line | cut -d"," -f4 | tr -d '"'`

	if (( $(echo "$trate > 200" | bc) ))
	then
		if (( $(echo "$pop > 10000000" | bc) ))
		then
			echo $state
		fi
	fi
done


