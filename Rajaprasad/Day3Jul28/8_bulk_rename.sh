#!/bin/bash

echo " bulk rename all file inside data directory"

x=1
for i in data/*.txt
do
	ext=`echo $i | cut -d"." -f2`
        path=`echo $i | cut -d"." -f1`
        mv $i $path$x"."$ext
        ((x++))
done


