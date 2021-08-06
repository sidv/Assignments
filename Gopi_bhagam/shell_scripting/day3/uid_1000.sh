
 
#!/bin/bash

file=`cat /etc/passwd | cut -d ":" -f1,3 --output-delimiter=":"`

for i in $file
do
	#echo $i
	file1=`echo $i | cut -d ":" -f1`
	file2=`echo $i | cut -d ":" -f2`
	echo $file1
	echo $file2
	if [[ $file2 -gt 1000 ]]
	then `echo $file1 > userid.txt`
	fi
done
