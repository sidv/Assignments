#!/bin/bash

echo  "find state more than 10000000 and rate -200"

for i in `cat cancer.csv | cut -d"," -f5,2|tr -d '"' `
do
	rate =`echo $i | cut -d"," -f2`
	population=`echo $i | cut -d"," -f2`
	if [[  $population -gt 10000000 && $rate -gt  -200  ]]
	then
		echo $i
	fi
done


