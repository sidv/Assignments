#!/bin/bash

IFS=$'\n'
for i in `ls -l`
do


	size=`echo $i | tr -s " " | cut -d" " -f5`
	name=`echo $i | tr -s " " | cut -d" " -f9`
 	if [[ -f $name ]] 
	then
		if [[ $size -gt 1000 ]]
		then
			echo $i
		fi
	fi
done
