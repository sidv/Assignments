#!/bin/bash

data="/home/ananthu/Linux_Training/shell_scripts/airlines.csv"

for i in `cat $data | cut -d"," -f6,7 | tr -d"" | grep "July"`
do
	if(($i>2009))
	then
		echo $i
	fi
done

