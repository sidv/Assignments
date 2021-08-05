#! /bin/bash
echo "Even or Odd"

read a

if (( $a % 2 == 0 ))
then
	echo $a" Even"
else
	echo $a" Odd"
fi
