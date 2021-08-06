#!/bin/bash


echo "Menu Driven"
echo "1.Addition 2.Subtraction 3.Multiplication 4.Division"
echo "Select any type"
read num

while (( num == 1 ))
do    echo "Read first Number"
        read num1
        echo "Read second Number"
        read num2
        sum=$(( num1+num2 ))
	echo "Sum is "$sum
done
while (( num == 2 ))
do    echo "Read first Number"
        read num1
        echo "Read second Number"
        read num2
        sub=$(( num1-num2 ))
        echo "Sub is "$sub
done
while(( num == 3 ))
do    echo "Read first Number"
        read num1
        echo "Read second Number"
        read num2
        mul=$(( num1*num2 ))
        echo "Mul is "$mul
done
while (( num == 4 ))
do    echo "Read first Number"
        read num1
        echo "Read second Number"
        read num2
        div=$(( num1/num2 ))
        echo "Div is "$div
done

