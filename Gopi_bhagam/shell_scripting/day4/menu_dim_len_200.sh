#! /bin/bash
echo "cars record where Dimensions.Length greater than 200"
cat cars.csv | while ifs= read l
do
	
	x=`echo $l | cut -d"," -f2 | sed 's/"//g'`
	if [[ x -gt 200 ]]
	then
		echo $l
	fi

done

