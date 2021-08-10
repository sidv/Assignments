#!/bin/bash

alpha="abcdefghijklmnopqrstuvwxyz"
echo $alpha
count=0
for dir in ./data$((count+1))
do
    echo $dir
    echo $dir/${alpha:$count:1}".txt"
    touch $dir/${alpha:$count:1}".txt"
    ((count++))
done
