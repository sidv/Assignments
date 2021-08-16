#!/bin/bash
num_lines=`cat aids.csv | wc -l`
cat aids.csv | tail -n $((num_lines -1)) | while read row
do
        new_infec_all_age=`echo $row | cut -d "," -f13 | tr -d '"'`
        new_infec_female=`echo $row | cut -d "," -f15 | tr -d '"' | tr -d "."`
        new_infec_female_r="${new_infec_female::-1}"
        #echo $new_infec_all_age
        if [[ $new_infec_all_age -le 100 ]]
        then
                 if [[ $new_infec_female_r -le 100 ]]
                then
	
                        echo $row 
                fi
        fi      

done
