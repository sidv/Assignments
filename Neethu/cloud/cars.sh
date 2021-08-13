#!/bin/bash


cat cars.csv|cut -d"," -f14|sort|uniq
