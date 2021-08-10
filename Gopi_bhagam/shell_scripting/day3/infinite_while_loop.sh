#! /bin/bash
echo ' create an infinite white loop'
while true
do
	echo ' 1. add'
	echo ' 2. sub'
	echo ' 3 . exit'
	read choice
	echo 'enter no'
	read n1
	echo 'enter no'
	read n2
	if [[ $choice -eq 1 ]]
	then
		echo 'The sum is' $((n1 + n2))
	elif [[ $choice -eq 2 ]]
	then
		echo 'The dif is' $((n1 - n2))
	elif [[ $choice -eq 3 ]]
	then
		exit
fi
done

