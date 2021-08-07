#!/bin/bash

echo "Check file permission"
read file
if [[ -r $file ]]
then
 echo "file is readable"
else
 echo "file is not readable"
fi
if [[ -w $file ]]
then
 echo "file is writable"
else
 echo "file is not writable"
fi
if [[ -x $file ]]
then
 echo "file is executable"
else
 echo "file is not executable"
fi

