#!/bin/bash

echo "----------Check file permission----------"

echo "Enter the file name"
read f
if [[ -e  $f ]]
then
	echo "File exist...!"
	if [[ -r $f  ]]
	then
		echo "$f is Readable"
	fi

	if [[ -w $f ]]
	then
		echo "$f is Writable"
	fi

	if [[ -x $f ]]
	then
		echo "$f in Executable"
	fi
fi
