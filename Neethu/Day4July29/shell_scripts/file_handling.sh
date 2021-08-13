#!/bin/bash

x=1
cat bio.txt | while read l 
do
	echo $x":"$l
	((x++))
done
echo "___________________________________"
x=1
while read l
do
	echo $x":"$l
	((x++))
done < bio.txt # pass the file using redirection operator
#_____________________________________________
