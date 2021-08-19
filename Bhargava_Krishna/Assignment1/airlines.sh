
#!/bin/bash
cat airlines.csv | while read row

do
	july=`echo $row | cut -d"," -f6 | grep "July" `
	year=`echo $row | cut -d"," -f7 | tr -d '"'`
	#echo $year 
	if [[ -n $july ]]
	then
		if [[ $year -gt 2009 ]]
		then 
			echo $row
		fi
	fi
done 
