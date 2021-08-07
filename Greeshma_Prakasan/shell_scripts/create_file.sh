#!/bin/bash

alphabet="a b c d e f g h i j k l m n o p q r s t u v w x y z"
#for i in $alphabet
#do
#	touch "data/"$i".txt"
#done
x=1
for i in data/*.txt
do
	ext=`ls -l $i | tr -s " " | cut -d" " -f9 | cut -d"." -f2`
	echo $ext
	path=`ls -l $i | tr -s " " | cut -d" " -f9 | cut -d"." -f1`
	echo $path
	echo $path$x$ext
	mv  $i $path$x$ext
	((x++))
done
