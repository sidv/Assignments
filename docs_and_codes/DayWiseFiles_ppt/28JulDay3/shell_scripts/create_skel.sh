#!/bin/bash



first_name="sid"
last_name="verma"
echo $first_name$last_name

#__________________________________________________________________________

echo "Creating skel"
log_path="/var/log/"
mkdir -p "project/public/images"
mkdir -p "project/public/js"
mkdir -p "project/screens"
mkdir -p "project/components"
mkdir -p $log_path"facebook" #/var/log/facebook
touch -p $log_path"facebook/app.log" #/var/log/facebook/app.log
touch "project/index.html"
echo "Write your code here" > "project/index.html"

