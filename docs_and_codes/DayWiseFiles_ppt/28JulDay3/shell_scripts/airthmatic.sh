#!/bin/bash

num1=10
num2=20

echo $num1 + $num2

echo $(( num1 + num2 ))
echo $(( num1 - num2 ))
echo $(( num1 * num2 ))
echo "_____________________________________"
c=$((num1+num2))
echo $c
