
#! /bin/bash
echo "cars record where identification.classification is automatic transmission and
identification.year greater than 2010" 
cat cars.csv | 
while read row
do
	iden=`grep 'Automatic transmission'`
        if [[ $iden -gt 2010 ]]
	then
		echo $row
	fi
done
