#!/bin/bash

while read l
do
	class=`echo $l |tr -s " "|tr -d '"' |cut -d"," -f12 `
	id_year=`echo $l |tr -s " "|tr -d '"' |cut -d"," -f16 `
#	echo $class $id_year
	if [[ $class == "Automatic transmission" ]]
	then
		if (( id_year > 2010 ))
		then
			echo $l 
		fi
	fi

done < cars.csv
