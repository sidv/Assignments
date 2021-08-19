#!/bin/bash

echo "Bulk renaming in progress...."

for i in superuser/*.txt
do
	file=`echo $i | cut -d"/" -f2
	path='echo $i | cut -d"/" -f1
	mv $i $path"/"$file
	

