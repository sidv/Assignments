
#!/bin/bash

len=`wc -l covid.csv | cut -d" " -f1`
declare -A death

cat covid.csv | tail -n $((len-1))|
(
	while read l
	do 

		dn=`echo $l | cut -d"," -f5 | tr -d '"'`
	 	c=`echo $l | cut -d"," -f6 | tr -d '"'`
		current_d=${death[$c]}
		death[$c]=$((current_d+dn))
	done
	for i in "${!death[@]}"
	do
		if [[ ${death[i]} -gt 200 && ${death[i]} -lt 300 ]]
		then
			echo $i
		fi
	done

)
