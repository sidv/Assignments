#! /bin/bash


x=1
for i in /home/superuser/Linux/*.txt

do
       file=`echo $i | cut -d"." -f11`
       ext=`echo $i | cut -d"." -f2`
       mv $i $file$x"."$ext 

       ((x++))
done
