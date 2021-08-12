#!/bin/bash

cat cars.csv | 
while read row
do
	identity=`grep 'Automatic transmission'`
        if [[ $identity -gt 2010 ]]
	then
		echo $row
	fi
done
