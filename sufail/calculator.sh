#!/bin/bash


echo "Menu Driven"
echo "1.Addition 2.Subtraction 3.Multiplication 4.Division"
echo "Select any type"
read num

sum(){
	echo "Read first Number"
        read num1
        echo "Read second Number"
        read num2
        sum=$(( num1+num2 ))
	echo "Sum is "$sum
}
sub(){
	echo "Read first Number"
        read num1
        echo "Read second Number"
        read num2
        sub=$(( num1-num2 ))
        echo "Sub is "$sub
}
mul(){
	echo "Read first Number"
        read num1
        echo "Read second Number"
        read num2
        mul=$(( num1*num2 ))
        echo "Mul is "$mul
}
div(){
	echo "Read first Number"
        read num1
        echo "Read second Number"
        read num2
        div=$(( num1/num2 ))
        echo "Div is "$div
}

 case $num in
 	'1') sum
 		;;
 	'2') sub
 		;;
 	'3') mul
 		;;
 	'4') div
 		;;
 	*) echo "Enter Valid Number"
 		;;
 esac
