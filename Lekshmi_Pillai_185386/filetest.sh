#!/bin/bash

echo "Read a file"
read file

if [[ -r $file ]]
then	echo "File Readable"
else echo "File is not Readable"
fi

if [[ -w $file ]]
then	echo "File is writable"
else echo "File is not writable"
fi

if [[ -x $file ]]
then echo "File is executable"
else echo "File is not executable"
fi
