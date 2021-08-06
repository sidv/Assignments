#!/bin/bash
sum(){
	a=$1
	b=$2
	echo $a" + "$b" = "$((a+b))
}

sub(){
        a=$1
        b=$2
        echo $a" - "$b" = "$((a-b))
}

mul(){
        a=$1
        b=$2
        echo $a" * "$b" = "$((a*b))
}

div(){
        a=$1
        b=$2
        echo $a" / "$b" = "$((a/b))
}



echo "enter the 1st num";read a
echo "enter the 2nd num";read b
echo "1 : Addition"
echo "2 : Substraction"
echo "3 : Multiplication"
echo "4 : Division"
echo "enter the choice";read c

case $c in
	1) sum $a $b
		;;
	2) sub $a $b
		;;
	3) mul $a $b
		;;
	4) div $a $b
		;;
esac
