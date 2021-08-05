#!/bin/bash

echo "odd or even "

echo " enter your number "

read num

if [[ '$num % 2' == 0 ]]
then 
	echo $num "is odd num "
else
	echo $num "is even num"

fi
