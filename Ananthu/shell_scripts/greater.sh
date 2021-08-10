#!/bin/bash

echo "Enter the first Number : "
read a
echo "Enter the second Number : "
read b
echo "Enter the third Number : "
read c
if [[ $a -gt $b && $a -gt $c ]]
then
	echo $a" is greater "
elif [[ $b -gt $a && $b -gt $c ]]
then
	echo $b" is greater"
else
	echo $c" is greater"
fi
