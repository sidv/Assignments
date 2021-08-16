#!/bin/bash

read a
read b

if (( a < b ))
then
	echo $a" is less than "$b
else
	echo $b" is less than "$a
fi
