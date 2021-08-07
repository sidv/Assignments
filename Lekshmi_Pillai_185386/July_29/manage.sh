#!/bin/bash


echo "Menu Driven"
echo "1.Start Firefox 2.Install Tree Package 3.Name to a file using cat command 4.Start gedit 5.Kill firefox using name 6.Kill gedit using name 7.Update software"
echo "Select any type"
read choice

case $choice in 
	'1') nice -n 8 firefox
		;;
	'2') sudo apt-get install tree
		;;
	'3') echo "Enter a name"
	     cat >names.txt
	     	;;
	'4') nice -n 3 gedit
		;;
	'5') pkill firefox
		;;
	'6') pkill gedit
		;;
	'7') sudo apt-get update
		;;
	*) echo "Enter a valid Choice"
		;;
esac

