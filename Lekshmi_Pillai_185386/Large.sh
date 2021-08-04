#!/bin/bash

echo "Read First Number"
read  num1

echo "Read Second Number"
read num2

echo "Read Third Number"
read num3

if [[ $num1 -gt $num2 && $num1 -gt $num3 ]]
then	echo $num1" is greater"
elif [[ $num2 -gt $num3 && $num2 -gt $num1 ]]
then	echo $num2" is greater"
else
	echo $num3 " is greater"

fi
