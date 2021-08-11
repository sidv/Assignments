#!/bin/bash

for i in ./data*
do
	cd $i
	touch a.txt b.txt c.txt
	cd ..
done
