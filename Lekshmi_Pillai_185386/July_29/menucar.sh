#!/bin/bash


echo "Menu Driven"
echo "1.Identification.Make is Audi "
echo "2.Engine Information Number of forward gera is less than user input "
echo "3.Dimensions height and width is greater than user input"
echo "Select any type"
read choice

case $choice in 
	'1') 
	     cat carss.csv | while read l
	     do
	     	make=`echo $l | cut -d "," -f14  | cut -d '"' -f2`
	     	echo $make
	     	if(( $make == "Audi" ))
	     	then echo $l
	     	fi
	     done
	     	;;
	 '2') echo "Read gear input"
	      read gear
	      cat carss.csv | while read l
	      do
	     	make=`echo $l | cut -d "," -f7  | cut -d '"' -f2`
	      if(( $make < $gear ))
	     	then echo $l
	      else
	        echo "Enter valid gear"
	     	fi
	     done
	     	;;
	  '3') echo "Dimension Height and width"
	       read height
	       read width
	       cat carss.csv | while read l
	       do
	     	heightt=`echo $l | cut -d "," -f1  | cut -d '"' -f2`
	     	widthh=`echo $l | cut -d "," -f3  | cut -d '"' -f2`
	     	echo $heightt
	     	if(( $heightt > $height &&  $widthh > $width ))
	     	then echo $l
	     	fi
	      done
	     	;;
	     
	 *) echo "Enter valid choice";;
esac

