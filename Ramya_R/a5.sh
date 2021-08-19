#! /bin/bash

echo "Calci operation"
while true
do
read a
read b

echo "Add 1"
echo "sub 2"
echo "mul 3"
echo "div 4"

echo "enter your choice c"
read c

if [[ $c -eq 1 ]]
then
echo "Add a+b" $((a+b))
elif [[ $c -eq 2 ]]
then
echo "sub a-b" $((a-b))
elif [[ $c -eq 3 ]]
then
echo "mul a*b" $((a*b))
elif [[$c -eq 4 ]]
then
echo "div a/b" $((a/b))
else
echo "No option"
fi

done
