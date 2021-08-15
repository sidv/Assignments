#!/bin/bash

echo "Reading input"
echo "Enter your name"
read name

echo "This is my name :"$name
echo "Enter num 1"
read a
echo "Enter num 2"
read b

echo "Sum is :"
echo $((a+b))
