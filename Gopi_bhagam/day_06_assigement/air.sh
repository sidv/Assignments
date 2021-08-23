#!/bin/bash

echo "finding airlines pattern"

for i in `cat airlines.csv | cut -d"," -f6,7 |tr -d '"' | grep "July" ` `
do 
	len=`echo $i | cut -d"," -f2`
	if [[ $len -gt 2009 ]]
	then
		echo $i

    	fi
done
