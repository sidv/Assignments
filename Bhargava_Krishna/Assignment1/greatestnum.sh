#! /bin/bash

echo "Enter number"
read a
echo "Enter number"
read b
echo "Enter number"
read c

if [[ $a -gt $b ]] && [[ $a -gt $c ]]
then
       echo $a"is greater than"$b and $c

elif [[ $b -gt $a ]] && [[ $b -gt $c ]]
then
       echo $b

else  
       echo $c

fi
   

