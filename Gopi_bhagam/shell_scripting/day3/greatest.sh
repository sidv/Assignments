#!/bin/bash
echo " Enter a number:"
read a
echo "ENter a number:"
read b
echo " Enter a  number :"
read c

if  [[ $a -gt $b && $a -gt $c  ]]
then
	echo $a" i greatest number"
elif [[ $b -gt $a && $b -gt $c ]]
then
	echo $b"is greatets number "
else 
	echo $c "i greatest number "
fi


