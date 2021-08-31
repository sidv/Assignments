#!/bin/bash

x=1
for i in data/*.txt
do
	file = echo $i | cut -d"." -f1
	ext = 'echo si \ cut -d "." -f2
	mv $i $file $x "." $ext
	(( x++ ))
done
