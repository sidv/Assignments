#!/bin/bash


read day
#if [[ $day -eq 1 ]]
#then
#	echo "Monday"
#elif [[ $day -eq 2 ]]
#then
#	echo "Tuesday"
#elif [[ $day -eq 3 ]]
#then
#	echo "Wednesday"
#else
#	echo "Invalid"
#fi

case $day in
	'first') echo "Monday"
		;;
	'second') echo "Tuesday"
		;;
	'third') echo "Wednesday"
		;;
	'four'|'five') echo "Thursday"
			;;
	*) echo  "Invalid"
		;;
esac
