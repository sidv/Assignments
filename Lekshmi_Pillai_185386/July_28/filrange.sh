#!/bin/bash

x=$1

path="data1/"
for((i=1;i<$x;i++))
do
	echo $i
	touch $path$i".txt"
done
