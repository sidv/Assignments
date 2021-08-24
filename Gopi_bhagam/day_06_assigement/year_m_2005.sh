
size=`cat aids.csv | wc -l`

cat aids.csv | tail -n $(( size -1 )) | while read line

do

	year=`echo $line | cut -d"," -f2 | tr -d '"'`
	adult=`echo $line | cut -d"," -f12 | tr -d '"'`

	if [[ $year -gt 2005  && $adult -gt 10000  ]]
	then
		echo $line
	fi


done
