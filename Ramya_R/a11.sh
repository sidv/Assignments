#! /bin/bash

echo "files"
i=1
x="123456789"
while [[ $i -le 10 ]]
do
echo $i".txt"
((i++))
done
