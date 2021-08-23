#!/bin/bash
#declare -A cars
#cat cars.csv | grep -n "" | grep -P '^[2|5]:' | while read row
#do
#	key=${row%:*}
#	value=${row#*:}
#	echo $value >> new_cars.csv
#	cars[$key]=$value
#done

#for i in ${cars[@]}
#do
#	echo $i
#done

declare -A cars
cat cars.csv |  while read row
do
       key=${row%:*}
       value=${row#*:}
#       echo $value >> new_cars.csv
       cars[$key]=$value
done

