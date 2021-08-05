#!/bin/bash

echo "menu driven calculator"

echo "Enter first number"
read num1
echo "Enter 2nd number"
read num2

echo "1.Addition"
echo "2.substraction"
echo "3.multiplication"
echo "4.division"
echo "5.exit"

echo "choose operation"
read op

if [[ $op -eq 1 ]]
then
	echo "addition operation starting ........"
	echo "$num1 "+" $num2 " = "$(( num1 + num2 ))"
elif [[ $op -eq 2 ]]
then
	echo "substraction operation started ......."
	echo " $num1 "-" $num2 "=" $(( num1 - num2 ))"
elif [[ $op -eq 3   ]]
then
	echo "Multiplication operation starting ......"
	echo "$num1 "*" $num2 "="$(( num1 * num2  ))"
elif [[ $op -eq 4  ]]
then
	echo "performing division operation"
	echo "$num1 "/" $num2 "="$(( num1 / num2 ))"
else
	exit
fi

