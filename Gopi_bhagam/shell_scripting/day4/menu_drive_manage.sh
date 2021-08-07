
#! /bin/bash
while true
do
	echo "Enter a choice"
	echo "1. start firefox"
	echo "2. Install tree package"
	echo "3. write your name to file "
	echo "4. start gedit"
	echo "5. kill firefox"
	echo "6. kill gedit"
	echo "7. update the software list"
	read choice
	case $choice in
		1.
			sudo nice -n -10 firefox
			;;
		2.
			sudo apt-get update
			sudo apt-get install tree
			;;
		3.
			echo "Enter your name"
			cat > file.txt
			;;
		4.
			sudo nice -n -9 gedit
			;;
		5.
			killall firefox
			;;
		6.
			killall gedit
			;;
		7.
			sudo apt-get update
			;;
		8.
			echo "Invalid"
			;;


	
done

