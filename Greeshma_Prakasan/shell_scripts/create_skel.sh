#!/bin/bash

mkdir -p "project/public/image"
mkdir -p "project/public/js"
mkdir -p "project/screens"
mkdir -p "project/components"
touch "project/components/index.html"
echo "write ur code here" > "project/components/index.html"
f=navin
l=reddy
echo $f$l >> "project/components/index.html"
log_path="project/components/"
mkdir -p $log_path"src"
