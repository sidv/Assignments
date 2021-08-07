#!/bin/bash

while read l
do
	len=`echo $l |tr -d '"' |cut -d"," -f2 `
	if (( $len > 200 ))
	then
		echo $l 
	fi

done < ~/Python_Training_UST/cars.csv
