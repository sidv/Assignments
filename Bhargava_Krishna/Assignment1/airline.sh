#! /bin/bash

cat airlines.csv | cut -d "," -f6 | head  -59 | tail -30

