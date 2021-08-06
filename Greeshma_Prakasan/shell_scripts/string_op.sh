#!/bin/bash

s="asfdfgkjhgfg"
echo $s
echo ${s}

echo ${s:0:3}
echo ${s:1:5}
echo ${s::4}
#echo ${}
echo ${s:(-1)}
echo ${s:(-4):(-1)}
echo ${s::-3}
echo ${s:(-3):2}

echo "length of string : "${#s}

#substitution
echo ${s//fg/mn}	#replace all occurance
echo ${s/fg/mn}		#replace 1st occurance

echo ${s/#as/mn}
echo ${s/%fg/mn}

file="data/file.txt"
echo ${file%.txt}	#remove suffix 
echo ${file%file.txt}
echo ${file%.txt}.doc
echo ${file#data/}	#remove prefix


echo ${s^^}		#convert to uppercase
echo ${s^}		#1st letter to uppercase

#convert to lowercase
data="ASDFGHJSDFG"
echo ${data,}
echo ${data,,}

multiline='this
is
a
string'

echo $multiline
