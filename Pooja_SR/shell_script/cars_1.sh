#!/bin/bash

cat cars.csv | while read row
do
	len='echo $row | cut -d"," -f2 |
