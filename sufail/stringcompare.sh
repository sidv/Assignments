#! /bin/bash

echo " Enter the word"
read  random

word = "Sufail"

if [[ $word == $random ]]
then
      echo "same string"
else
      echo "not match"
fi
