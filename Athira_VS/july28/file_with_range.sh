#!/bin/bash

count=1
echo "Enter the maximum range for the file"
read range
if ((range<1))
then
	echo "Enter a valid number. It must be greater than 0"
else
	while ((count<=range))
	do
		touch $count".txt"
		((count++))
	done
fi	

