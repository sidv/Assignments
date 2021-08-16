count=`cat covid.csv|wc -l`
declare -A death_dict

cat covid.csv|tail -n $((count-1))|
(
    while read line
    do
        death=`echo $line|tr -s " "|cut -d"," -f5|tr -d '"'`
        country=`echo $line|tr -s " "|cut -d"," -f6|tr -d '"'`
        cur_death=${death_dict[$country]}
        death_dict[$country]=$((cur_death+death))
    done

    for ctry in "${!death_dict[@]}"
    do

        if (( death_dict[$ctry] > 200 && death_dict[$ctry] < 300 ))
        then
            echo $ctry
        fi
    done 
)
