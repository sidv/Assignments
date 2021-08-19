#!/bin/bash

echo "Menu Driven Programming"
echo "1. Create Files"
echo "2. Delete Files"
echo "3. Enter your name"

echo "Enter your choice"
read choice

case $choice in 
	"1") echo "Enter input"
	     read n
	     for ((i=1;i<=n;i++))
	     do
	     	touch $i".txt" 
	     done
	     	;;
	"2") echo "Which file to be delete?"
	     read n
	      rm $n".txt"
	     ;;
	"3") echo "Enter your name"
	     cat > names.txt
	     ;;
	"*") echo "Invalid Number"
             ;;
esac
	     

