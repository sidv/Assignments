#!/bin/bash

numb=`cat aids.csv | wc -l`
cat aids.csv | tail -n $(( numb - 1 )) | while read line
do
        comp=100
	comp2=100
        all=`echo $line | cut -d"," -f13 | tr -d '"'`
	fem=`echo $line | cut -d"," -f15 | tr -d '"'`	
	fem1=`echo $fem | cut -d"." -f1` 
        if [[ $all -lt $comp ]]
        then   
        	if [[ $fem1 -lt $comp2 ]]
 		then
			echo $line
		fi
	fi	
done



