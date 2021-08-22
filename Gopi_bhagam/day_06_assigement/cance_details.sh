
len=`cat cancer.csv | wc -l`

cat cancer.csv | tail -n $(( len-1 )) | while read line

do

	pop=`echo $line | cut -d"," -f4 | tr -d '"'`
	if [[ ${pop%.*} -gt 10000000  ]]
	then
		rate=`echo $line | cut -d"," -f2 | tr -d '"'`
		if [[ ${rate%.*}  -gt 200 ]]
		then
			echo $line | cut -d"," -f1 | tr -d '"'
		fi
	fi

done
