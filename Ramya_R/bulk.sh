echo "bulk rename"
for i in dataScr/*.txt
do
text=`echo $i | cut -d"." -f2
a=`echo $i | cut -d"." -f1
file=`echo $i | cut -d"/" -f2`
path=`echo $i | cut -d"/" -f1`
mv $i $a$x$text
((x++))
done
