#i/bin/bash

echo "Enter the number"
read number
if (( $number % 2 == 0 ))
then
	echo $number" is even number "
else
	echo $number" is odd number"
fi
