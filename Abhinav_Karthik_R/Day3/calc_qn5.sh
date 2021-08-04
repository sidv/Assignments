#i/bin/bash

echo " ______________calculator_____________"

echo "Press 1 for Addition"
echo "Press 2 for Subtraction"
echo "Press 3 for Multiplication"
echo "press 4 for Division"
read choice

echo "Enter the First number"
read first
echo "Enter the Second number"
read second

if [[ $choice -eq 1 ]]
then
	echo $((first+second))"is the answer"
elif [[ $choice -eq 2 ]]
then
	echo $((first-second))" is the answer"
elif [[ $choice -eq 3 ]]
then
	echo $((first*second))" is the answer"
elif [[ $choice -eq 4 ]]
then
	echo $((first/second))" is the answer"
else
	echo " please enter correct choice"
fi
