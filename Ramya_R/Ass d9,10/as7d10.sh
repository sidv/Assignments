#! /bin/bash                                                                     

lines=`cat aids.csv | wc -l`
cat aids.csv| tail -n $(( lines - 1 )) | while read line
do
        adults=`echo $line | cut -d"," -f12 | tr -d '"'`
        year=`echo $line | cut -d"," -f2 | tr -d '"'`
if [[ $year -gt 2005 ]]
then      
 #if [[ $adults -gt 10000 ]]
if [[ $adults -eq 10000 ]]  
      then
                            echo $line
                fi
       fi

done


