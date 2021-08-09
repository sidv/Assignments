#!/bin/bash


echo "Menu Driven"
echo "1.Addition 2.Subtraction 3.Multiplication 4.Division"
echo "Select any type"
read num

if (( num == 1 ))
then    echo "Read first Number"
        read num1
        echo "Read second Number"
        read num2
        sum=$(( num1+num2 ))
	echo "Sum is "$sum
fi
if (( num == 2 ))
then    echo "Read first Number"
        read num1
        echo "Read second Number"
        read num2
        sub=$(( num1-num2 ))
        echo "Sub is "$sub
fi
if (( num == 3 ))
then    echo "Read first Number"
        read num1
        echo "Read second Number"
        read num2
        mul=$(( num1*num2 ))
        echo "Mul is "$mul
fi
if (( num == 4 ))
then    echo "Read first Number"
        read num1
        echo "Read second Number"
        read num2
        div=$(( num1/num2 ))
        echo "Div is "$div
fi

