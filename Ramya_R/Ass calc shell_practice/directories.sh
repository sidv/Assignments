#! /bin/bash                                                                    

i=1

while [[ $i -le 10 ]]
do
mkdir -p data$i
((i++))
done



