#!/bin/bash
echo 'enter three nums'
read a
read b
read c
if [[ $a -gt $b && $a -gt $c ]]
then
	echo $a' is greatest.'
fi
if [[ $b -gt $a && $b -gt $c ]]  
then
        echo $b' is greatest.'
fi
if [[ $c -gt $b && $c -gt $b ]]  
then
        echo $c' is greatest.'
fi
