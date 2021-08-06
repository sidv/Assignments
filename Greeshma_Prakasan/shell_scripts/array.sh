#!/bin/bash
names=('sid' 'ann' 'ben' 'zen' 'anu' 'john')

echo ${names[@]}
echo ${#names[@]}

echo ${names}
echo ${#names}

echo ${names[2]}
echo ${#names[2]}

echo ${names[@]:2:2}
