#! /bin/bash

echo "Calci operation"
while true
do
read a
read b

sum(){
echo "sum is " $((a+b))
}
sub(){
echo "sub is " $((a-b))
}
mul(){
echo "mul is " $((a*b))
}
div(){
echo "div is $ "$((a/b))
} 
echo "Add 1"
echo "sub 2"
echo "mul 3"
echo "div 4"

echo "enter your choice c"
read c

if [[ $c -eq 1 ]]
then
#echo "Add a+b" $((a+b))
sum 
elif [[ $c -eq 2 ]]
then
sub
elif [[ $c -eq 3 ]]
then
mul
elif [[$c -eq 4 ]]
then
div
else
echo "No option"
fi

done
