#!/bin/bash

num=$1
i=1
while [[ $i -le 10 ]]
do
	echo $((i*num))
	((i++))
done
echo "______________________________________________"

while true
do
	echo "Press 1 for add"
	echo "Press 2 for subtract"
	echo "Press 3 for exit"
	read choice
	read num1
	read num2
	if [[ $choice -eq 1 ]]
	then
		echo $((num1+num2))
	elif [[ $choice -eq 2 ]]
	then
		echo $((num1-num2))
	elif [[ $choice -eq 3 ]]
	then
		exit
	fi

done
