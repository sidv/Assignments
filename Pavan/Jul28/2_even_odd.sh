#!/bin/bash

echo "finding out even odd number"

echo "Enter a number to check for even or odd"
read num

if (( num == 0 ))
then
echo	"$num is not even nor odd"

elif (( num % 2 == 0  ))
then
	echo "$num is an even number"
else
	echo "$num is an odd number"
fi
