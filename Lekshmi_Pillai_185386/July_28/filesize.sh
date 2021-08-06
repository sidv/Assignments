#!/bin/bash


file=`ls -l|tr -s " "|cut -d " " -f5,9 --output-delimiter=":"`
for i in $file
do
	echo $i
	file1=`echo $i|cut -d ":" -f1`
	file2=`echo $i|cut -d ":" -f2`
	if (( $file1 > 1000 ))
	then echo "Hi - "$file2 
	fi
done

