#! /bin/bash

echo "Enter the file name"
read file

if [[ -e $file ]]
then
     echo $file"exists"
     if [[ -r $file ]]
     then
           echo $file "is readable"
     fi

     if [[ -w $file ]]
     then
           echo $file "is writable"
     fi
     if [[ -x $file ]]
     then
           echo $file "is executable"
     fi
fi 
