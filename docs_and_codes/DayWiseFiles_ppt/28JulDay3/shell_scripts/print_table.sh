#!/bin/bash

num=$1

for ((i=0;i<10;i++))
do
	echo $((i*num))
done
echo "_______________________________________________"

#1,2,3,4,5,6,7,8,9,10

for i in {1..10..3}
do
	echo $((i*num))
done
