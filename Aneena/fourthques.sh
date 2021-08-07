#!/bin/bash

echo " Current location files and name"
echo "Enter two numbers"
read a
read b
echo "1.Addition"
echo "2.Subtraction"
echo "3.Multiplication"
echo "4.Division"
echo "Enter your choice"
read choice

if [[ $choice -eq 1 ]]
then 
echo "Sum :" $((a+b))
elif [[ $choice -eq 2 ]]
then
echo "Sub :" $((a-b))
elif [[ $choice -eq 3 ]]
then
echo "Mul :" $((a*b))
elif [[ $choice -eq 4 ]]
then
echo "Div :" $((a/b))
else
exit
fi

