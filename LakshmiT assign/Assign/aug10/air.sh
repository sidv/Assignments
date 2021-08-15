#!/bin/bash
num_lines=`cat aids.csv | wc -l`
cat aids.csv | tail -n $((num_lines -1)) | while read row
do
        year=`echo $row | cut -d "," -f2 | tr -d '"'`
	infec=`echo $row | cut -d "," -f12 | tr -d '"'` 
	#echo $infec
        #echo $year
        if [[ $year -gt 2005 ]]
        then
                if [[ $infec -gt 10000 ]]
		then
			
			echo $row
		fi
        fi	

done
