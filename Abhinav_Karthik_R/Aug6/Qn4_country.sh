#!/bin/bash

cat aids.csv | while read l
do
        people=`echo $l | cut -d"," -f18 | sed 's/"//g'`
	country=`echo $l | cut -d"," -f1 | sed 's/"//g'`
        if [[ $people -gt 100000 ]]
        then
                echo $country
        fi
done
