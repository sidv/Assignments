#!/bin/bash

echo "Enter the file name"
read file

if [[ -r $file ]] 
then
	echo "File is readable"

	if [[ -w $file ]]
	then
		echo "File is writable"

		if [[ -x $file ]]
		then
			echo "file is executable"
		
		fi
	fi
fi
