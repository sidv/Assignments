
#!/bin/bash

len=`cat covid.csv | wc -l`

cat covid.csv | tail -n $(( len-1 )) | while read line

do

        death=`echo $line | cut -d"," -f5 | tr -d '"'`
        if [[ ${death%.*} -gt 200  && ${death%.*}  -lt 300 ]]
        then
              echo $line | cut -d"," -f6 | tr -d '"'
               
        fi

done

 
