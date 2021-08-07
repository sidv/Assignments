#!/bin/bash

cat airlines.csv | cut -d"," -f6,7 | grep 'July' > flight_data.txt

