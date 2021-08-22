#!/bin/bash


sum(){
	echo "Addition"
	read a
	read b
	echo $((a+b))
}

sub(){
	echo "Substraction"
	read a
	read b
	echo $((a-b))
}

sub
