#!/bin/bash

echo "----------------Odd or Even--------------"

echo "Enter a number"
read n
if (( $n % 2 == 0  ))
then
	echo $n "is Even"
else
	echo $n" is Odd"
fi
