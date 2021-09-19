#!/bin/bash

echo "check the file is readable,writable and executable"

echo "Enter file name"
read file


if  [[ -e $file  ]]
then
	echo "$file exists"
	if [[ -d $file   ]]
	then
		echo "$file is a directory we need to give file name !"
	else
		echo "$file is a file"
		if [[ -x $file ]]
		then
			echo "$file is executable"
		        if  [[ -w $file  ]]
			then
				echo "$file is writable"
				if [[ -r $file ]]
				then
					echo "$file is readable"
				fi
			fi
		fi
	fi
else
	echo "$file not exists"
fi
