#!/bin/bash

count=`cat aids.csv|wc -l`

cat aids.csv|tail -n $((count-1))|while read line
do
	year=`echo $line|tr -s " "|cut -d"," -f2|tr -d '"'`
	if ((year>2007))
	then
		echo $line
	fi
done
