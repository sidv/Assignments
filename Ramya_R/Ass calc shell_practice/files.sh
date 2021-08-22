#! /bin/bash                                                                                                                                                 

i=1

while [[ $i -le 10 ]]
do
touch data$i"/a.txt"
touch data$i"/b.txt"
touch data$i"/c.txt"

((i++))
done


