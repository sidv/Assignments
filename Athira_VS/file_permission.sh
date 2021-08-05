#!/bin/bash

echo "Enter a file name"
read file

if [[ -e $file ]] #file exists
then
	if [[ -r $file  ]]
	then 
		echo $file" is readable"
	fi
	if [[ -w $file ]]
	then
		echo $file" is writable"
	fi
	if [[ -x $file ]]
	then
		echo $file" is executable"
	fi
fi
