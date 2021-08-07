#! /bin/bash
IFS=$'\n'
for i in `ls -l`
do
echo $i
size=`echo $i | tr -s " " | cut -d" " -f5`
if [[ -f $i ]]
then
if [[ $size -gt 1000 ]]
then
echo $i
fi
fi
done
