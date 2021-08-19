#!/bin/bash

name=$1

if [[ -e $name]]
then
	if [[ -f $name ]]
	then
		sort $name | uniq | tee $name".new"
	fi
fi
