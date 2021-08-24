
#!/bin/bash


line=`wc -l aids.csv | cut -d" " -f1`

cat aids.csv | tail -n $(( line -1 )) | while read l
do

        allage=`echo $l | cut -d"," -f13 | tr -d '"'`
        female=`echo $l | cut -d"," -f15 | tr -d '"'`
        if [[ $allage -lt 100 && ${female%.*} -lt 100 ]]
        then
                echo $l
	fi
done
