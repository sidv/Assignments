#! /bin/bash
echo "menu driven using functions"
echo "1.Add"
echo "2.Sub"
echo "3.Mul"
echo "4.Div"
read choice
echo "enter the no"
read x
echo "enter the no"
read y
if [[ $choice -eq 1 ]]
then
	sum(){

        echo "sum is"$(( x+y ))
	}
	sum
fi
if [[ $choice -eq 2 ]]
then
	diff(){
	echo "sub  is"$(( a-b ))
	}
	diff
fi	
if [[  $choice -eq 3 ]]
then 
	mul(){
	echo "mul is"$(( a*b ))
	}
	mul
fi
if [[ $choice -eq 4 ]]
then
	div(){
	echo "div is"$(( a/b ))
	}
	div
fi

