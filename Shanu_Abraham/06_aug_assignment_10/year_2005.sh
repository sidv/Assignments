#! /bin/bash

cat aids.csv | while read row
do
	year=`echo $row | cut -d ',' -f2 | tr -d  '"'`
	infection=`echo $row | cut -d ',' -f12 | tr -d '"'`
	if [[ $year -gt 2005 ]]
	then
		if [[ $infection -gt 10000 ]]
		then
			echo $infection"infec"
			echo $year"year"
			echo $row
		fi
	fi
done
