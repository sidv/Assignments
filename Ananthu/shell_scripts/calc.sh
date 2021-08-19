#!/bin/bash

echo "--------CALCULATOR----------"
echo "Choose Any Operation "
echo "1.Add"
echo "2.Subtract"
echo "3.Multiply"
echo "4.Divide"
read oper
echo "Enter the first number"
read a
echo "Enter the second number"
read b

if [[ $oper -eq 1 ]]
then
	sum=$((a+b))
	echo "The sum is "$sum
elif [[ $oper -eq 2  ]]
then
	diff=$((a-b))
	echo "The difference is "$diff
elif [[ $oper -eq 3  ]]
then
        pro=$((a*b))
        echo "The product is "$pro
elif [[ $oper -eq 4  ]]
then
        quo=$((a/b))
        echo "The quotient is "$quo

fi
