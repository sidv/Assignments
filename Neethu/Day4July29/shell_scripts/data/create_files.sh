#!/bin/bash

alphabet="abcdefghijklmnopqrstuvwxyz"

#for i in "${alphabet[@]}"
#do
#	echo $i
	
#done

for ((i=0;i<${#alphabet};i++))
do
	echo "${alphabet:$i:1}"
	touch ${alphabet:$i:1}".txt"
done
