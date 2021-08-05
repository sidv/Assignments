#!/bin/bash


ls -l| grep '^-' |tr -s " "| cut -d" " -f5,9 > file_name_size.txt
while read size file
do
	if ((size>1000))
	then
		echo $file
	fi
done < file_name_size.txt

#size=`ls -l| grep '^-' |tr -s " "| cut -d" " -f5,9|cut -d" " -f1`
#file_name=`ls -l| grep '^-' |tr -s " "| cut -d" " -f5,9|cut -d" " -f2`

#for i in $size
#do
#	if ((i>1000))
#	then
#		echo $i
#	fi

#done


