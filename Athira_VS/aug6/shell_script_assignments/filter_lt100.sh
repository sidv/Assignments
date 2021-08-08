#!/bin/bash

count=`cat aids.csv|wc -l`

cat aids.csv|tail -n $((count-1))|while read line
do
	all_age=`echo $line|tr -s " "|cut -d"," -f13|tr -d '"'`
	female_adult=`echo $line|tr -s " "|cut -d"," -f15|tr -d '"'|cut -d"." -f1`

	if (( all_age<100 && female_adult<100 ))
	then
		echo $line
	fi
done
