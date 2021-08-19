#!/bin/bash

sum(){
	a=$1
	b=$2
	echo $#
	echo $@
	echo "Sum is"$((a+b))
}


sub(){
	a=$1
	b=$2
	echo "Sub is $((a-b))"
}

mul(){
	a=$1
	b=$2
	echo $((a*b))
}

sum $1 $2 #Calling function

result=$(mul 10 20) #return value
echo $result

echo "Muliplication is $(mul 10 20)"
#list=`ls`
#list=$(ls)
#result=`mul $1 $2`
#result=$(mul $1 $2)










