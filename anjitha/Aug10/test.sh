
#!/bin/bash

len=`wc -l covid.csv | cut -d" " -f1`
#declare -A death
death=("dummy")
cat covid.csv | tail -n $((len-1))|
(
	while read l
	do 

		dn=`echo $l | cut -d"," -f5 | tr -d '"'`
	 	c=`echo $l | cut -d"," -f6 | tr -d '"' `
		death+=($c)
		echo $death

	done
#	echo $death
)
