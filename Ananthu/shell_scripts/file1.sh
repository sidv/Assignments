#!/bin/bash

ls -l
ls -l | tr -s " " | cut -d" " -f1,9

