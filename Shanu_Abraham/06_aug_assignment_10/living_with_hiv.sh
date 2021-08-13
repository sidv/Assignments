#! /bin/bash
cat aids.csv | while read row
do
	live_with_hiv=`echo $row | cut -d "," -f22 | tr -d '"'`
	country=`echo $row | cut -d "," -f1 | tr -d '"'`
	if [[ live_with_hiv -gt 100000 ]]
	then
		echo $live_with_hiv"hiv"
		echo $country
	fi
done
