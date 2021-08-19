#!/bin/bash

al="a b c"

for i in data/*
do 
	for j in $al
	do
		touch $i"/"$j".txt"
	done
done
