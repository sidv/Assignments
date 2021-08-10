#!/bin/bash

cat aids.csv | while read l
do
        age=`echo $l | cut -d"," -f13 | sed 's/"//g'`
        female=`echo $l | cut -d"," -f15 | sed 's/"//g' | cut -d"." -f1`
        if [[ $age -lt 100 && $female -lt 100 ]]
        then
                echo $l
        fi
done
