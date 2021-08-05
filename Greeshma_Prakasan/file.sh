#!/bin/bash
echo "inside the script"
read file
echo $file" read file"
if [[ -f $file ]]
then
	echo $file" exists"
	if [[ -r $file ]]
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
