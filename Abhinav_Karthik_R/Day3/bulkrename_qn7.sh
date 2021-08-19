#i/bin/bash

file=`ls *.txt`
x=1
for i in $file
do
	name=`echo $i | cut -d"." -f1 `
	ext=`echo $i | cut -d"." -f2 `
	mv $i $name$x"."$ext
	((x++))
done
