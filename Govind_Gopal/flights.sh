
#!/bin/bash

string="July"
numb=2009

IFS=','
for i in `cat airlines.csv`
do
	string="July"
	numb=2009

	month=`cat airlines.csv | tr -d '"'| cut -d"," -f6`
	year=`cat airlines.csv | tr -d '"'| cut -d"," -f7`
	if [[ $year -eq $numb ]]  
	then
		echo "its almost there"
	fi
done
