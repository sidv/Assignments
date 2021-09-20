#!/bin/bash

echo "current location files permission and name"
ls -l| tr  -s " " | cut -d" " -f1,9

