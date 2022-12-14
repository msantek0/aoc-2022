#!/bin/bash
echo $1
mkdir $1

cd $1
file=$1".py"
touch $file
touch example.txt
touch input.txt