#i/bin/bash

echo "Enter the range"
read range
for ((i=1;i<=range;i++))
do
	touch $i.txt
done

