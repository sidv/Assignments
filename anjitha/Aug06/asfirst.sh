

#!/bin/bash


line=`wc -l aids.csv | cut -d" " -f1`

cat aids.csv | tail -n $(( line -1 )) | while read l
do

	year=`echo $l | cut -d"," -f2 | tr -d '"'`
	#echo $year
	if [[ $year -gt 2007 ]]
	then
		echo $l
	fi


done
