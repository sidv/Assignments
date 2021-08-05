
#!/bin/bash

while true
do
	echo "SELECT ONE "
	echo "a) All cars where Identification.Make is Audi"
	echo "b) All cars where Engine Information Number of forward gear is less than desired value"
	echo "c)All cars where Dimensions.Width and Dimensions.Height are greater than desired value"
	read choice

	case $choice in
		a)	cat cars.csv | while read l
			do
				a=`echo $l | cut -d"," -f14 | sed 's/"//g'`
				if [ "$a" == "Audi" ]
				then
					echo $l
				fi

			done < new_cars.csv
			;;
		b)
			echo "Enter Number of gears"
			read gears
			cat cars.csv | while read l
                        do
                                a=`echo $l | cut -d"," -f7 | sed 's/"//g'`
                                if [[ $a -lt $gears ]]
                                then
                                        echo $l
                                fi

                        done < new_cars.csv
			
			;;
		c)
			echo "Enter Height"
			read height
			echo "Enter Width"
			read width
                        cat cars.csv | while read l
                        do
                                ah=`echo $l | cut -d"," -f1 | sed 's/"//g'`
				aw=`echo $l | cut -d"," -f3 | sed 's/"//g'`
                                if [[ $ah -gt $height ]]
                                then
					if [[ $aw -gt $width ]]
					then
                                        	echo $l
					fi

                                fi

                        done < new_cars.csv

			;;

		*)
			echo "Invalid"
			;;
	esac
done
