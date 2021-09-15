#!/bin/bash

numb=`cat aids.csv | wc -l`
cat aids.csv | tail -n $(( numb - 1 )) | while read line
do
        comp=100000
	comp2=100
        all=`echo $line | cut -d"," -f22 | tr -d '"'`
 
        if [[ $all -gt $comp ]]
        then
       		country=`echo $line | uniq |  cut -d"," -f1 | tr -d '"'`
		echo $country

	fi	
done



