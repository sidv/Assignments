#!/bin/bash


file_name_size=`ls -l| grep '^-' |tr -s " "| cut -d" " -f5,9 --output-delimiter=':'`
#echo $file_name_size

for i in $file_name_size
do 
	size=`echo $i|cut -d":" -f1`
	file=`echo $i|cut -d":" -f2`
	if ((size>1000))
	then
		echo $size $file
	fi

done
#for i in `ls -l| grep '^-' |tr -s " "| cut -d" " -f5,9`
#do
#	size=`echo $i|cut -d" " -f1`
#	file=`echo $i|cut -d" " -f1`
#	echo "size $size file $file"
#done
