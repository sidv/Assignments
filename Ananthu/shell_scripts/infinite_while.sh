#! /bin/bash
echo 'Infinite While loop'
while true
do
	echo 'press 1 for add'
	echo 'press 2 for sub'
	echo 'press 3 for exit'
	read choice
	echo 'Enter the first number :'
	read num1
	echo 'Enter the second number :'
	read num2
	if [[ $choice -eq 1 ]]
	then
		echo 'The sum is' $((num1 + num2))
	elif [[ $choice -eq 2 ]]
	then
		echo 'The difference is' $((num1 - num2))
	elif [[ $choice -eq 3 ]]
	then
		exit
fi
done
