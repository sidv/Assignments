




#!/bin/bash

add(){
	echo $num1 + $num2 = $(( num1 + num2 ))
}

sub(){
	echo $num1 - $num2 = $(( num1 - num2 ))
}

mul(){
	echo $num1 "*" $num2 = $(( num1 * num2 ))
}

div(){
	echo $num1 / $num2 = $(( num1 / num2 ))
}


while true
do
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
	echo "5. Exit"
	echo "Select a number from 1 to 5 for the operation"
	read option

	if [[ $option -eq 1 ]]
	then
		add num1 num2
	elif [[ $option -eq 2 ]]
	then
		sub num1 num2
	elif [[ $option -eq 3 ]]
	then
        	mul num1 num2
	elif [[ $option -eq 4 ]]
	then
		if (( num2 == 0))
		then
			echo "Can't divide by Zero."
		else 
			div num1 num2
		fi
	elif [[ $option -eq 5 ]]
	then
		exit

	else
		echo "Invalid Option. Please choose a number between 1 and 4"
	fi
done
