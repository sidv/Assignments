ize=`cat aids.csv | wc -l`

cat aids.csv | tail -n $(( size -1 )) | while read line


do
        people=`echo $line | cut -d"," -f18 | tr -d '"'`
	country=`echo $line | cut -d"," -f1 | tr -d '"'`
        if [[ $people -gt 100000 ]]
        then
                echo $country
        fi
done
