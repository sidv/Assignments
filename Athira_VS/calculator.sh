#!/bin/bash

echo "Calculator"
echo "-------------"

echo "Enter the 1st number"
read num1
echo "Enter the 2nd number"
read num2

echo "MENU"
echo "1. Addition"
echo "2. Subtraction"
echo "3. Multiplicattion"
echo "4. Division"
echo "Select a number from 1 to 4 for the operation"
read option

if [[ $option -eq 1 ]]
then
	echo $num1 + $num2 = $(( num1 + num2 ))
elif [[ $option -eq 2 ]]
then
	echo $num1 - $num2 = $(( num1 - num2 ))
elif [[ $option -eq 3 ]]
then
        echo $num1 "*" $num2 = $(( num1 * num2 ))
elif [[ $option -eq 4 ]]
then
	if (( num2 == 0))
	then
		echo "Can't divide by Zero."
	else 
		echo $num1 / $num2 = $((num1 / num2))
	fi
else
	echo "Invalid Option. Please choose a number between 1 and 4"
fi
