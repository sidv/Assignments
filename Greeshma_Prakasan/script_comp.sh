#!/bin/bash
echo "enter the word"
read random
word="hello"

if [[ $word == $random ]]
then
	echo "it is same"
else
	echo "it is not same"
fi
