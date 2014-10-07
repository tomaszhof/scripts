#!/bin/sh

cd $1 $2
FILES=$( find . -type f -name "*.jpg" | cut -d/ -f 2)
mkdir temp && cd temp 
for file in $FILES; do 
    BASE=$file
    convert -compress jpeg -quality 32 -density 300x300 ../$BASE $BASE.pdf;
    done
pdftk *pdf cat output ../$2 && 
cd .. 
rm -rf temp
