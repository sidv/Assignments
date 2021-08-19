#!/bin/bash

echo "Enter a  number :"
read num


if [[ $num%2==0 ]]
then
	echo $num " even number " 
else 
	echo $num " odd number  "
fi
