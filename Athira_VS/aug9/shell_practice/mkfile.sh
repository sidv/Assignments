#!/bin/bash

alpha="abcdefghijklmnopqrstuvwxyz"
count=0
for i  in {1..26}  
do
    dir="data"$((count+1))
    if [[ -d $dir ]]
    then
        #    echo $dir/${alpha:$count:1}".txt"
        touch $dir/${alpha:$count:1}".txt"
        ((count++))
    fi
done
