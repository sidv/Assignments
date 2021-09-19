#! /bin/bash
echo "cars record where Dimensions.Length greater than 200"
cat cars.csv | while IFS=, read l
do
	
	a=`echo $l | cut -d"," -f2 | sed 's/"//g'`
	if [[ a -gt 200 ]]
	then
		echo $l
	fi

done

