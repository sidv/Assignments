#!/bin/bash

echo " create 10 directories"
for (( i=1;i<=10;i++ ))
do
	dir="data"$i
	mkdir $dir
done

