#!/bin/bash
x=1
cat bio.txt | while read l
do
	echo $x" : "$l
	((x++))
done

echo "*****************************************"
x=1
while read l
do
	echo $x" - "$l
done < bio.txt
