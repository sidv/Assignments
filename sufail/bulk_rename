#!/bin/bash

x=1

for i in data/*.txt
do
	file=`echo $i | cut -d "/" -f2`
	path=`echo $i | cut -d "/" -f1`
	filesplit=`echo $file | cut -d "." -f1`
        filesplit2=`echo $file | cut -d "." -f2`
	mv $i $path"/"$filesplit$x"."$filesplit2
	((x++))
done
