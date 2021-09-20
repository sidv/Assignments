#!/bin/bash

lines=`cat cars.csv | wc -l`

cat cars.csv|tail -n $((lines-1))| while read l
do
        len=`echo $l | cut -d "," -f2`
        len=`echo $len | cut -d '"' -f2`
        if(( $len > 200 ))
        then
                echo $l
        fi
done
