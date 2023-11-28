#!/bin/bash

for ((i=0; i<=8; i++))
do
    for ((j=i+1; j<=9; j++))
    do
        printf "%d%d" $i $j

        if [ $i -ne 8 ] || [ $j -ne 9 ]; then
            echo -n ", "
        else
            echo
        fi
    done
done
