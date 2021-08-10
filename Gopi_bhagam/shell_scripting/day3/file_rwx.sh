#!/bin/bash
echo "Enter a file name :" 
read file

if [[ -f $file ]]
then
	echo $file " file exits "
	if [[ -r $file ]]
	then
		echo $file " readable "
		if [[ -w $file ]]
		then
			echo $file " writeable "
			if [[ -x $file ]]
			then
				echo $file " excutable "
			fi
		fi
	fi
fi
				
