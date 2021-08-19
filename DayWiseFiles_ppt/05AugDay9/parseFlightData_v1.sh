#!/bin/bash

IFS=$'\n'
for i in `cat airlines.csv`
do
	month=`echo $i | cut -d"," -f6 | tr -d '"'`
        year=`echo $i | cut -d"," -f7 | tr -d '"'`
        if [[ $month == 'July' ]]
        then
                if [[ $year -gt 2009 ]]
                then
                        echo $i >> data.txt
                fi
        fi

done

