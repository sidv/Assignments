#! /bin/bash
for i in ./*
do
cat /etc/passwd | cut -d":" -f1,4 | grep '[1-9]000' >> users.txt 
done
