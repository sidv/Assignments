#!/bin/bash

count=`cat aids.csv|wc -l`

cat aids.csv|tail -n $((count-1))|while read line
do
	year=`echo $line|tr -s " "|cut -d"," -f2|tr -d '"'`
	adult=`echo $line|tr -s " "|cut -d"," -f12|tr -d '"'`

	if (( year>2005 && adult > 10000 ))
	then
		echo $line
	fi
done
