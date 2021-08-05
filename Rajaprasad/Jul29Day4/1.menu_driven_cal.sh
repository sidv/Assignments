#! /bin/bash
echo "menu driven using functions"
echo "1.Addition"
echo "2.Subtraction"
echo "3.Multiplication"
echo "4.Division"
read choice
echo "enter the no"
read a
echo "enter the no"
read b
if [[ $choice -eq 1 ]]
then
	sum(){
	echo "dfdgf"
        echo "sum is"$(( a+b ))
	}
	sum
fi
if [[ $choice -eq 2 ]]
then
	diff(){
	echo "diff is"$(( a-b ))
	}
	diff
fi	
if [[  $choice -eq 3 ]]
then 
	mul(){
	echo "multiplication is"$(( a*b ))
	}
	mul
fi
if [[ $choice -eq 4 ]]
then
	div(){
	echo "division is"$(( a/b ))
	}
	div
fi

