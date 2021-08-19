#! /bin/bash

echo "Enter two numbers"
read a
read b

echo "1. Addition"
echo "2. Substraction"
echo "3. Multiplication"
echo "4. Division"

echo "Enter your Choice"

read choice

if [[ $choice -eq 1 ]]
then
     echo "sum is:" $((a+b))

elif [[ $choice -eq 2 ]]
then
     echo "Sub is:" $((a-b))
elif [[ $choice -eq 3 ]]
then
     echo "Mul is:" $((a*b))
elif [[ $choice -eq 4 ]]
then
     echo "Div is:" $((a/b))
else
     exit
fi
