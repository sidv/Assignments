#!/bin/bash

file_path=/home/veena/Python_Training_UST/july28/data
count=1
for i in $file_path/*.txt
do
	file=` echo $i | cut -d"." -f1 `
	extn=` echo $i | cut -d"." -f2 `
	mv $i $file$count"."$extn
	(( count++))

done


