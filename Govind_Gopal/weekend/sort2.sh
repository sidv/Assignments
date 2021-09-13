#!/bin/bash

numb=`cat aids.csv | wc -l`
cat aids.csv | tail -n $(( numb - 1 )) | while read line  
do
        comp=2007
	comp2=10000
        year=`echo $line | cut -d"," -f2 | tr -d '"'`
	inf=`echo $line | cut -d"," -f12 | tr -d '"'`	
 
        if [[ $year -gt $comp ]]
        then   
        	if [[ $inf -gt $comp2 ]]
 		then
			echo $line
		fi
	fi	
done



