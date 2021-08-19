#! /bin/bash
echo "Greatest number"
echo "enter the no"
read a
echo "enter the no"
read b
echo "enter the no"
read c
if [[ $a -gt $b  && $a -gt $c ]]
then
	echo $a'is greater no'
	elif [[ $b -gt $a && $b -gt $c ]]
	then
		echo $b'is the greater no'
		else
			echo $c'is greater no'
fi
