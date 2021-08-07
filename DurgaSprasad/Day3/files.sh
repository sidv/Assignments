#!/bin/bash

echo " creating ...... multiple files inside data directory"

path="./data"

for i in {a..e}
do 
	touch $path/$i.txt
	echo $i.txt
done
