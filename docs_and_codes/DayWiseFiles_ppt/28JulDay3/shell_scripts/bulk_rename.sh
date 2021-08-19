#!/bin/bash

echo "Bulk rename"
echo "Appending counting number in name"
x=1
#for i in data/*.txt
#do
#	mv $i $i$x   #mv data/a.txt data/a.txt1
#	((x++))
#done

echo "____________________________________________"
for i in data/*.txt
do
	file=`echo $i | cut -d"/" -f2`
	path=`echo $i | cut -d"/" -f1`
	mv $i $path"/"$x$file  #mv data/a.txt data/1a.txt
	((x++))
done



