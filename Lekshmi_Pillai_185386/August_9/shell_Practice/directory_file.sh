#!/bin/bash
path="/home/superuser/Python_Training_UST/August_9/Assignments/shell_Practice"

for i in $path"/data"*
do
	cd $i
	touch a.txt b.txt c.txt
done


