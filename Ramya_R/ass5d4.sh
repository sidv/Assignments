#! /bin/bash                                                                    


lines=`cat cars.csv | wc -l`
cat cars.csv | tail -n $((lines -l)) | while read row
do

aq(){
echo cat cars.csv | grep "Audi"
}

bq(){
read n
l=`echo $row | cut -d"," -f7 | tr -d '"'`
if [[ $l -gt $n ]]
then 
echo $row
fi
}

cq(){
read w
dw=`echo $row | cut -d"," -f3 | tr -d '"'`
if [[ $dw -gt $w ]]
then
echo $row
fi
}

dq(){
read h
dh=`echo $row |cut -d"," -f1 | tr -d '"'`
if [[ $dh -gt $h ]]
then
echo $row
fi
}

echo "aq 1"
echo "bq 2"
echo "cq 3"
echo "dq 3"
echo "enter your choice c"
read c

if [[ $c -eq 1 ]]
then
aq
elif [[ $c -eq 2 ]]
then
bq
elif [[ $c -eq 3 ]]
then
cq
elif [[$c -eq 4 ]]
then
dq
else
echo "No option"
fi
done
