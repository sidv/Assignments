#!/bin/bash

echo "Findout the greatest number among all three numbers"

echo "Enter first num: "
read first

echo "Enter 2nd num : "
read second

echo "Enter third num: "
read third

if [[ $first -gt $second && $first -gt $third ]] 
then
	echo "$first is a gteatest number"
elif [[ $second -gt $first && $second -gt $third ]] 
then
	echo "$second is a greatest number"
else
	echo "$third is the greatest number"
fi
