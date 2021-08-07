
#! /bin/bash
while true
do
	echo "Enter a choice"
	echo "a) start firefox"
	echo "b) Install tree package"
	echo "c) write your name to file "
	echo "d) start gedit"
	echo "e) kill firefox"
	echo "f) kill gedit"
	echo "g) update the software list"
	read choice
	case $choice in
		a)
			sudo nice -n -10 firefox
			;;
		b)
			sudo apt-get update
			sudo apt-get install tree
			;;
		c)
			echo "Enter your name"
			cat > file.txt
			;;
		d)
			sudo nice -n -9 gedit
			;;
		e)
			killall firefox
			;;
		f)
			killall gedit
			;;
		g)
			sudo apt-get update
			;;
		*)
			echo "Invalid"
			;;


	esac
done

