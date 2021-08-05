#!/bin/bash


user_name_id=`cat /etc/passwd |cut -d":" -f1,3`
#echo $file_name_size

for i in $user_name_id
do 
	name=`echo $i|cut -d":" -f1`
	id=`echo $i|cut -d":" -f2`
	if ((id>1000))
	then
		echo $name >> users.txt
	fi

done
#for i in `ls -l| grep '^-' |tr -s " "| cut -d" " -f5,9`
#do
#	size=`echo $i|cut -d" " -f1`
#	file=`echo $i|cut -d" " -f1`
#	echo "size $size file $file"
#done
