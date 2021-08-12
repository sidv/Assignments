#!/bin/bash


echo " enter user input :"

read inp
asd=1

for i in $(seq $asd $inp)

do
	touch $i.txt

done
