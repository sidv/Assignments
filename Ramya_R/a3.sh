#! /bin/bash

echo "Read, write, executable file"

read file

if [[ -e $file ]]
 then
 echo $file" exists"
  if [[ -r $file ]]
 then
    echo $file" is readable"
  
    if [[ -w $file ]]
    then
    echo $file" is writable"
    
if [[ -x $file ]]
then
echo $file " is executable"
fi
fi
fi
fi

