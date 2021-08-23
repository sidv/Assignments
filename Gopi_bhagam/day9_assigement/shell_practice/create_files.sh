#! /bin/bash                                                        

echo " create a.txt b.txt and c.txt inside each directory"

for i in {a..c}
do
	for j in {1..10}
	do
		cd "data"$j
		touch $i."txt"
		cd ../
	done
done

