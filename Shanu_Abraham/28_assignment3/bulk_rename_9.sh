#! /bin/bash
echo 'data/a.txt------------------->data/a1.txt'

x=1
for i in data/*.txt
do
	echo $i
	fil=`echo $i| cut -d '.' -f1` #data/a
	echo $fil
	#file=`echo $i| cut -d '/' -f2`| cut -d '.' -f1 
	mv $i $fil$x'.txt'
	((x++))
done
