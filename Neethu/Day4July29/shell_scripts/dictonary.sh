#!/bin/bash

declare -A employees
employees['sid']="pune"
employess['neha']="noida"
employees['rajat']="mumbai"


declare -A states #Declare variable
#Its key value pair. Here we dont have index. We access all elements by key unlike normal array
#Other name associative array
#UP->lucknow
#MP->bhopal
states['UP']="lucknow" #
states['MP']="bhopal"
states["MH"]="Mumbai"

#print  dictionary
echo ${states[@]} #get all elements (value)
echo ${!states[@]} #Get all keys 
echo "____________________________________________"
#Length of dictionary
echo ${#states[@]}

echo "_____________________________________"
#Delete element
unset states['MP']
echo ${states[@]}
echo ${!states[@]}

echo "______________________________________"
echo ${states[UP]} #Fetch value of one key
