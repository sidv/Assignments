#! /bin/bash

cat aids.csv | while read line 
do
	
	year=`echo $line | cut -d "," -f2 | tr -d '"'`
	#echo $year
	if [[ $year -gt 2007 ]]
	then
		echo  $line"if function"
	fi
done
