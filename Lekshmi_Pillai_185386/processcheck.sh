#!/bin/bash


lines=`ps -e | wc -l` 
ps -e | tail -n $((lines-1)) | while read l
do 
	process=`echo $l | cut -d " " -f1,4 --output-delimiter=":"`
	#echo $process
	processid=`echo $process|cut -d ":" -f1`
        processname=`echo $process|cut -d ":" -f2`
        if (( $processid > 1000 ))
        then echo "Hi - "$processname
        fi

done
