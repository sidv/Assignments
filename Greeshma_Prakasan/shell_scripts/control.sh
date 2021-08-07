#!/bin/bash

echo "______________________readinput________________"
read name
echo "my name is "$name
echo "____________________if block__________________"
num=10
if [[ num -gt 15 ]];then
	echo "inside if block"
fi

echo "enter 1st no"
read a
echo "enter 2nd no"
read b
if [[ a -gt b ]]
then
	echo $a" is greater than "$b
fi

echo "______________________if else block________________________"

if [[ a -lt b ]]
then
	echo $a" less than "$b
else
	echo $b" less than "$a
fi

echo "______________________if else block________________________"

if [[ a -eq b ]]
then
        echo $a" equal to "$b
elif [[ a -gt b ]]
then
	echo $a" greater than "$b

else
        echo $b" greater than "$a
fi

echo "___________________use (()) in if block______________"
if ((a == b))
then
	echo $a" is equal to "$b
fi
