#!/bin/bash


echo "enter your file path"

read file


if [[ -e $file ]]
then 
	echo $file"exists"
fi
if [[ -r $file ]]
then
	echo $file" file is readable"
fi
if [[ -w $file ]]
then
	echo $file" file is writable"
fi
if [[ -x $file ]]
then
        echo $file" file is executable"
fi

