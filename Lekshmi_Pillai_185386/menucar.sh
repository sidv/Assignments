#!/bin/bash


echo "Menu Driven"
echo "1.Identification.Make is Audi "
echo "2.Engine Information Number of forward gera is less than user input "
echo "3.Dimensions height and width is greater than user input"
echo "Select any type"
read choice

case $choice in 
	'1') 
	     IFS= $'\n'
	     files=`cat carss.csv | cut -d "," -f14,15`
	     for i in $files
	     do 
	     echo $i
	     	#make=`echo $i | cut -d ":" -f1`
	     	#make=`echo $make | cut -d '"' -f2`
		#id=`echo $i | cut -d ":" -f2`
		#echo $make
		#echo $id
	     	#if(( $make == Audi ))
	     	#then echo "Audoo"
	     	#fi
	     done
	     	;;
	     
	 *) ;;
esac

