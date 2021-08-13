#!/bin/bash

#Declaration
names=('Siddhant' 'Rajat' 'Neha' 'Raja' 'Pooja') #All elements must be space seperated
#	  0	    1       2      3      4
#        -5        -4      -3     -2     -1
#Get array value
echo ${names[@]} #Return all elements as a seperate word
echo ${names[*]} #return all elements as a single word

echo ${names} #Returns first index string
echo "______________________________________"
#Get Index value
echo ${names[2]} #Second index value
echo ${names[-4]} #-fourth index value
echo "_____________________________________"
#Length of array
echo ${#names[@]} #All elements count. No of elements

echo ${#names} #Length of first index
echo ${#names[3]} #Length of 3 index
echo "_____________________________________"

#Slicing of array
echo ${names[@]:2:2} # Slicing array
#{variable[@]:startIndex:count}
echo ${names[@]:1:3}

#Append new element
names=("${names[@]}" 'sid')
echo ${names[@]}
names+=('anubhav')
echo ${names[@]}

#Delete array element
unset names[3]
echo ${names[@]}

#Modify value of index
names[1]="Mark"
echo ${names[@]}

