
#!/bin/bash

echo " choose your option -> addition = 1, subtraction = 2, multiplication = 3 and division = 4 "
read fun

add=1
sub=2
mul=3
div=4

if [[ $fun -eq $add ]]
then
	echo "enter the first number "
	read a
	echo "enter the second number"
	read b
	echo "The sum is"
	echo $(( a + b )) 
elif [[ $fun -eq $sub ]]
then
	echo "enter the first number"
	read a
	echo "enter the second number"
	read b
	echo $(( a - b )) "is the difference"
elif [[ $fun -eq $mul ]]
then
	echo "enter the first number"
	read a
	echo "enter the seocnd number"
	read b
	echo $(( a * b )) "is the result"
elif [[ $fun -eq $div ]]
then
	echo "enter the first number"
	read a
	echo "enter the second number"
	read b
	echo $(( a / b )) "is the result"

fi

