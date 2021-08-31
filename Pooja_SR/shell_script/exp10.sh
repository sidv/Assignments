#!/bin/bash

while true
do
	echo 'enter 1 for addition'
	echo 'enter 2 for substration'
	echo 'enter 3 for division'
	echo 'enter 4 for multiplication'
	echo 'enter 5 for exiting'
read a
echo 'enter the desired two numbers'
read numb1
read numb2
if [[ $a -eq 1]]
then
echo $(( num1+num2 ))
elif [[ $a -eq 2 ]]
then
echo $(( num2-num2 ))
elif [[ $a -eq 3 ]]
then
echo $(( num/num2 ))
elif [[ $a -eq 4 ]]
then
echo $(( num1*num2 ))
elif [[ $a -eq 5 ]]
then
exit
fi
	
