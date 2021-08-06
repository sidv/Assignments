#!/bin/bash

sum(){
	echo "Addition"
	read a
	read b
	echo $((a+b))
}
#sum

sub(){
	a=$1
	echo $a
	b=$2
	echo $((a+b))
}
sub $1 $2

