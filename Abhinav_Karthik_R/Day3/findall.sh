#i/bin/bash

files=`ls -l | tr -s " " |cut -d" " -f5,9`
echo $files
for i in $files
do
	#size=`echo $i | cut -d" " -f1`
	#name=`echo $i | cut -d" " -f2`
	echo $i
done

