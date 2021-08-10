#!/bin/bash

for j in {a..c}
do
	for i in {1..10}
	do
		cd "data"$i
		touch $j.txt
		cd ..
	done
done



