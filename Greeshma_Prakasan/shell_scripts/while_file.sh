#!/bin/bash
IFS=','
a=1,2,3,4,5
for i in $a
do
	echo $i
done
