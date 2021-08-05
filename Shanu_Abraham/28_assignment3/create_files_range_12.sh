#! /bin/bash
echo "command line arguments"
range=$1


for  (( i=1;i<=range;i++ ))
do
	touch $i".txt"
done

