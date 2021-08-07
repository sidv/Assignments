#! /bin/bash

cat airlines.csv | cut -d "," -f7 | tail -1945 > datas.txt
