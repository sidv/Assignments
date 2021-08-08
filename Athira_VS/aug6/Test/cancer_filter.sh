#!/bin/bash

count=$(cat cancer.csv|wc -l)

cat cancer.csv |tail -n $((count-1))| while read line
do
	state=`echo $line|tr -s " "|cut -d"," -f1|tr -d '"'`
	population=`echo $line|tr -s " "|cut -d"," -f4|tr -d '"'|cut -d'.' -f1`
	rate=`echo $line|tr -s " "|cut -d"," -f2|tr -d '"'|cut -d'.' -f1`
	rate_precisn=rate=`echo $line|tr -s " "|cut -d"," -f2|tr -d '"'|cut -d'.' -f2`
	if(( (population>10000000 && rate>200)||(population>10000000 && rate==200 && rate_precisn>0)))
	then
		echo $state
	fi

done
