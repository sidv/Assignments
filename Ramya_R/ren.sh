#! /bin/bash

echo "rename"

for i in dataScr/*txt
do
t=`echo $i | cut -d"." -f1`
text=`echo $i | cut -d"." -f2`
file=`echo $i | cut -d"/" -f2`
path=`echo $i | cut -d"/" -f1`
#mv $i $path"/"$text$x$file
mv $i $t$x"."$text
((x++))
done
