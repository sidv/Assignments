#! /bin/bash

cat aids.csv | while read row
do
	infec=`echo $row | cut -d "," -f13 | tr -d '"'`
	female_infec=`echo $row | cut -d "," -f15 | tr -d '"' | tr -d '.0'`
	if [[ $infec -lt 100 ]]
	then
		if [[ $female_infec -lt 100 ]]
		then
			echo $infec"infec"
			echo $female_infec"female"
			echo $row
		fi
	fi
done
