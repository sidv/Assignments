#!/bin/bash

echo "___________________________If Block______________________________"

#if [[ condition ]] 
#then
#	echo "Write expression here if true"
#fi

echo "Enter Number"
read a
echo "Enter number"
read b

if [[ $a -lt $b ]]
then
	echo $a" is less than "$b
fi

echo "_____________________________________________________________"
echo "If-else block"
echo "Enter Number"
read a
echo "Enter number"
read b

if [[ $a -gt $b ]]
then
	echo $a" is greater than "$b
else
	echo $b"is greater than "$a
fi

echo "_______________________________________________________"
echo "Elif Block"

echo "Enter Number"
read a
echo "Enter number"
read b

if [[ $a -eq $b ]] ;then
        echo $a" is equal to "$b
elif [[ $a -gt $b ]];then
 	echo $a" is greater than"$b
else
	echo $b" is greater than "$a
fi




