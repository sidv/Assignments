#! /bin/bash

lines=`cat cars.csv | wc -l`
cat cars.csv | tail -n $((lines -l)) | while read row
do
len=`echo $row | cut -d"," -f2 | tr -d '"'`
if [[ $len -gt 200 ]]
then
echo $row
fi
done
