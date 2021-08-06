#!/bin/bash
echo "enter the 1st number"
read a
echo "enter the 2nd number"
read b
echo "enter the option"
echo "1 - Addition"
echo "2 - Substraction"
echo "3 - multiplication"
echo "4 - division"
read o
if [[ o -eq 1 ]];then
	c=$((a + b))
	d="+"
elif [[ o -eq 2 ]];then
	c=$((a - b))
	d="-"
elif [[ o -eq 3 ]];then
	c=$((a * b))
	d="*"
elif [[ o -eq 4 ]];then
	c=$((a / b))
	d="/"
fi
echo $a$d$b" = "$c
