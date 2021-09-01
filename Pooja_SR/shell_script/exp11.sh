#!/bin/bash
echo 'enter the required range'
read range
for (( i=0 ; i < $range; i++ ))
do
	echo $i'.xt'
	mkdir data/$i.txt
done
exit
