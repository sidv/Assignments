#i/bin/bash

myfile="myfile.txt"

if [[ -r $myfile ]]
then
	echo " file is readable "
else
	echo "file is not readable"

fi
if [[ -w $myfile ]]
then
	echo "file is writable"
else
	echo "file is not writable"
fi
if [[ -x $myfile ]]
then
	echo "file is executable"
else
	echo "file is not executable"
fi
