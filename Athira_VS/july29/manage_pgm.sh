#!/bin/bash

while true
do

	echo "_________MENU_________"
	echo "1. Start firefox"
	echo "2. Install tree"
	echo "3. Write name to file"
	echo "4. Start gedit"
	echo "5. Kill firefox using name"
        echo "6. Kill gedit"
	echo "7. Update software list"
	echo "8. Exit"
	echo "Select an option from 1 to 8"
	echo " "
	echo " "

	read choice
	
	case $choice in 
		'1')	echo "Starting Firefox"
			gnome-terminal --command=firefox
				;;
		'2') 	sudo apt-get update
			sudo apt-get install tree
				;;
		'3')	echo "Enter your name"
			read name
			echo $name > name.txt
			echo "Wrote $name to name.txt file"
				;;
		'4')	gnome-terminal --command=gedit
				;;
		'5')	echo "Killing firefox"
			killall firefox
				;;
		'6')	echo "Killing gedit"
			killall gedit
				;;	
		'7')	sudo apt-get update
				;;	
		'8')	exit
				;;
		'*')	echo "Invalid"
				;;
	esac
		     		
done
