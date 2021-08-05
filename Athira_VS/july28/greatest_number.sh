#!/bin/bash

echo "Enter num1"
read num1
echo "Enter num2"
read num2
echo "Enter num3"
read num3

if [[ $num1 -gt $num2 ]]
then
	if [[ $num1 -gt $num3 ]]
	then
		echo $num1" is the greatest number"
	else
		echo $num3" is the greatest number"
	fi
elif [[ $num2 -gt $num3 ]]
then
	echo $num2" is the greatest number"
else
	echo $num3" is the greatest number"
fi


