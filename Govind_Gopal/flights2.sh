#!/bin/bash

cat airlines.csv | tr -d '"' | cut -d',' -f6 > plane.txt		
IFS=$'/n'
for i in plane.txt
do
	str="July"
	if [[ $i == "str" ]]
	then
	echo $i
	fi
done

