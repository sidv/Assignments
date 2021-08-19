#!/bin/bash

user=`whoami`
d=`date`

echo `date` >> data.txt
echo `whoami` >> data.txt

#fetch_data `ip a show wlo1 | tr -s " " | grep 'inet '| cut -d" " -f3| cut-d"/" -f1`
