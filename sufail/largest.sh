#!/bin/bash

echo "Enter First Number"
read  num1

echo "Enter Second Number"
read num2

echo "Enter Third Number"
read num3

if [[ $num1 -gt $num2 && $num1 -gt $num3 ]]
then	echo $num1" is greater"
elif [[ $num2 -gt $num3 && $num2 -gt $num1 ]]
then	echo $num2" is greater"
else
	echo $num3 " is greater"

fi
