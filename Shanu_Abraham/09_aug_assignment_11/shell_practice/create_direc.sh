#!/bin/bash

echo "Program to create 10 directories data1,data2,data3 and so on"
for (( i=1;i<=10;i++ ))
do
	dir="data"$i
	mkdir $dir
done
