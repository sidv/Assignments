#!/bin/bash

echo "Enter the first number"
read a
echo "Enter the second number"
read b
echo "enter the third number"
read c

if [[ $a -gt $b && $a -gt $c ]];then
	echo $a" is greatest"

elif [[ $b -gt $a && $b -gt $c ]];then
	echo $b "is greatest"

else 
	echo $c "is greatest"
fi

