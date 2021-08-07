#!/bin/bash

while true
do

	echo "_________MENU_________"
	echo "1. All cars where Identification.Make is Audi"
	echo "2. All cars where Number of Forward Gears is less than the given value"
	echo "3. All cars where Dimensions.Width and Dimensions.Height is greater than given value"
	echo "4. Exit"
	echo "Select an option from 1 to 4"
	echo " "
	echo " "

	read choice
	
	case $choice in 
		'1')	rm -f new_cars.csv
			cat cars.csv|while read l
			do
				make=`echo $l |tr -s " "|tr -d '"' |cut -d"," -f14 `
						
				if [[ $make == "Audi" ]]
				then
					echo $l >> new_cars.csv
				fi

			done 
				;;
		'2') 	echo "Enter maximum number of forward gears"
			read max
			rm -f new_cars.csv
                        cat cars.csv|while read l
                        do
                                gears=`echo $l |tr -s " "|tr -d '"' |cut -d"," -f7 `

				if (( gears < max  ))
                                then
                                        echo $l >> new_cars.csv
                                fi

                        done
				;;
		'3')	echo "Enter minimum width"
			read min_width
			echo "Enter minimum height"
                        read min_height

                        rm -f new_cars.csv
                        cat cars.csv|while read l
                        do
                                height=`echo $l |tr -s " "|tr -d '"' |cut -d"," -f1 `
				width=`echo $l |tr -s " "|tr -d '"' |cut -d"," -f3 `

                                if (( height > min_height && width > min_width  ))
                                then
                                        echo $l >> new_cars.csv
                                fi

                        done

				;;
		'4')	exit
				;;
		'*')	echo "Invalid"
				;;
	esac
		     		
done
