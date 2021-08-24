size=`cat aids.csv| wc -l`

cat aids.csv | tail -n $(( size-1 )) |  while read line

do
        age=`echo $line | cut -d"," -f13 | tr -d '"'`
        female=`echo $line | cut -d"," -f15 | tr -d '"'`
        if [[ $age -lt 100 && $female -lt 100 ]]
        then
                echo $line
        fi
done
