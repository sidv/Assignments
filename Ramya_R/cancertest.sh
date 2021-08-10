#! /bin/bash                                                                                                                                                  

lines=`cat cancer.csv | wc -l`
cat cancer.csv| tail -n $(( lines - 1 )) | while read line
do
        peop=`echo $line | cut -d"," -f4 | tr -d '"'`
	rate=`echo $line | cut -d"," -f2 | tr -d '"'`
if [[ ${peop%.*} -gt 10000000 ]]
then
                if [[ ${rate%.*} -gt 200 ]]
                then
                        echo $line | cut -d"," -f1 | tr -d '"'
                fi
fi
done


