#!/bin/bash

echo "Enter first number"
read first
echo "Enter Second Number"
read second
echo "Enter Third number"
read third
if [[ $first -gt $second && $first -gt $third ]]
then
	echo $first"is the greatest number"
elif [[ $second -gt $third ]]
then
	echo $second"is the greatest number"
else
	echo $third"is the greatest number"
fi
