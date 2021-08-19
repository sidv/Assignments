#!/bin/bash


read file #read file name

if [[ -e $file ]] # Check file exists
then
	echo $file" exists"
	if [[ -d $file ]] #check file is directory
	then
		echo $file" is a directory"
	else
		echo $file" is a file"
		if [[ -x $file ]] #check file is executable
		then
			echo $file" is executable"
		fi
	fi
fi

#if [[ -x $file ]]
#then
#	echo $file" is executable"
#fi
read file2 #read another filename

if [[ $file -ef $file2 ]] # Check files are same or not
then
	echo $file" is same as "$file2
else
	echo $file"is not same as"$file2
fi
