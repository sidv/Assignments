#!/bin/bash
 
echo "Enter Two numbers : "
read num1
read num2
 
# Input type of operation
echo "1. Addition"
echo "2. Subtraction"
echo "3. Multiplication"
echo "4. Division"
read cho


if [[ $cho == 1 ]]
then
	echo "output is :"$(( num1 + num2 ))
elif [[ $cho == 2 ]]
then
        echo "output is :"$(( num1 - num2 ))
elif [[ $cho == 3 ]]
then
        echo "output is  :"$(( num1 * num2 ))
elif [[ $cho == 4 ]]
then
        echo "output is  : "$(( num1 / num2 ))

else 
	echo "invalid choic"

fi


