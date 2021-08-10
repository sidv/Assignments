#!/bin/bash
     #87654321 With negative symbol || Count -->
     #01234567   
name="Siddhant"
multiline_str="This
is
sid
"
echo $name  #print string
echo ${name} #print string
#Length
echo ${#name}
echo "_________________________________"
#Slicing Use this to get substring
echo ${name:0:3} #slicing #ouput = sid
echo ${name:2:4} #${variable:start index: count of char}
echo ${name::3} #First index you dont need to mention
echo ${name:4:} #Invalid
echo ${name:4}
echo ${name:(-1)}
echo ${name:(-4):2}
echo ${name::-3}
echo ${name:2:(-3)}
echo "___________________________________"
#Substitution
echo ${name//dd/hh} # Replace all occurance ${variable//from/to}
echo ${name/dd/hh} #Replace first occurance ${varible/from/to}

echo ${name/#Si/di} # Replace from font(prefix)
echo ${name/%nt/as} # Replace from suffix(back)
echo "__________________________________"

#Manupulation
file="data/a.txt"
echo ${file%.txt} #removes the suffix(backside) ${variable%string}
echo ${file%a.txt}
echo ${file%.txt}".doc" #data/a.doc

echo ${file%/a.txt} 
echo ${file%/*}

echo ${file#data/} # removes the prefix(frontside)
echo "___________________________________"
#Change case
#Change to uppercase
data="sid"
echo ${data^^} #Change all letters to uppercase
echo ${data^} #Chnage first letter to upper case
echo "___________________________________"
#Change to lower case
data="SID"
echo ${data,}
echo ${data,,}

a=10
name="sid"
echo $a" is number"
echo "$a is number"
echo '$a is number'




