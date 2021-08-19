#! /bin/bash                                                                                                                                           

lines=`cat aids.csv | wc -l`
cat aids.csv| tail -n $(( lines - 1 )) | while read line
do
        num=`echo $line | cut -d"," -f22 | tr -d '"'`

                if [[ $num -gt 100000 ]]
                then
                        echo $line | cut -d"," -f1 | tr -d '"'
                fi

done


