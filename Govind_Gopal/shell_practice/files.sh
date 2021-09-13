#!/bin/bash

#for (( i = 1 ; i < 11 ; i ++ ))
#do
i=1	
	for o in {a..j}
	do 
		touch ~/shell_practice/data$i/$o.txt
		$((i++))
	done
#done

