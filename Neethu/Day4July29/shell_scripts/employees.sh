#!/bin/bash

declare -A employees

while true;
do
	echo "1.Add employee"
	echo "2.Delete employee"
	echo "3.Display all employee"
	echo "4.Search employee"
	read choice
	case $choice in
		'1') echo "Adding employee"
			read name
			read place
			employees[$name]=$place
			;;
		'2') echo "Deleting employee"
			read name
			unset employees[$name]
			;;
		'3') echo "All employees details"
			echo "${employees[@]}"
			;;
		'4') echo "Employee details"
			read name
			echo ${employees[$name]}
			;;
		*) echo "Invalid"
			;;
	esac


done
