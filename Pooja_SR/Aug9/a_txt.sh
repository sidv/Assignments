#!/bin/bash
#write a shell script to create  a.txt ,b.txt inside each diaractory you created in qs 11
i=1
for f in {a..j}
do
	touch ~/shell_practice/data$i/$f.txt
	$((i++))
done

