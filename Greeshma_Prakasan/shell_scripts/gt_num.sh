#!/bin/bash

echo "enter the 1st number"
read a
echo "enter the 2nd number"
read b
echo "enter the 3rd number"
read c
if [[ a -ge b && a -ge c ]]
then
	echo $a"is greater"
elif [[ b -ge a && b -ge c ]]
then
	echo $b"is greater"
else
	echo $c"is greater"
fi
