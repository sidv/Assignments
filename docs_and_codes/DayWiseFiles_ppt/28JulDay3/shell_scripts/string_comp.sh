#!/bin/bash

echo "Guess random word"
echo "Enter word"
read random

if [[ -z $random ]]
then
	echo "You forgot to enter the word"
fi

word="Hello"
if [[ $word == $random ]]; then
	echo "You Got correct word"
else
	echo "Oops! This is wrong"
fi
