
#!/bin/bash


line=`wc -l aids.csv | cut -d" " -f1`

cat aids.csv | tail -n $(( line -1 )) | while read l
do

        total=`echo $l | cut -d"," -f22 | tr -d '"'`
        if [[ $total -gt 100000 ]]
        then
              country=` echo $l | cut -d"," -f1 | tr -d '"'`
	      echo $country,$total        
	fi
done
