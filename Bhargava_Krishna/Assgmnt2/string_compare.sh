#! /bin/bash

echo " Guess random word"
echo " Enter the word"
read  random

word = "Hello"

if [[ $word == $random ]]
then
      echo "yu got correct word"
else
      echo "oops"
fi
