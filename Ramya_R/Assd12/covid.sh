#! /bin/bash                                                                                                                                                

lines=`cat covid.csv | wc -l`
cat covid.csv| tail -n $(( lines - 1 )) | while read line
do
        deaths=`echo $line | cut -d"," -f5 | tr -d '"'`
if [[ $deaths -gt 200 && $deaths -lt 300 ]]
then                  
             echo $line | cut -d"," -f6 | tr -d '"'
               
       fi

done
