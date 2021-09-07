#!/bin/bash


sum(){
	echo "Addition"
	read a
	read b
	echo $(( a+b ))
}
sub(){
	echo "substraction"
	read a
	read b
	echo $(( a-b ))
}
mul(){
	echo "multiplication"
	read a
	read b
	echo $(( a*b ))
}
div(){
	echo "division"
	read a
	read b
	echo $(( a/b ))
}
sum
sub
mul
div
