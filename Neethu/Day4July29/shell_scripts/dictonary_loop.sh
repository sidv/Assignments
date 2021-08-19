#!/bin/bash

declare -A employees
employees['sid']="pune"
employess['neha']="noida"
employees['rajat']="mumbai"


declare -A states #Declare variable
#Its key value pair. Here we dont have index. We access all elements by >
#Other name associative array
#UP->lucknow
#MP->bhopal
states['UP']="lucknow" #
states['MP']="bhopal"
states["MH"]="Mumbai"


for i in "${states[@]}" #Iterate through values
do
	echo $i
done

for i in "${!states[@]}" #Iterate through keys
do
	echo $i
done
