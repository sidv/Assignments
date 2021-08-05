#!/bin/bash

ls -l | grep -P '^-'| tr -s " " | cut -d" " -f1,9

