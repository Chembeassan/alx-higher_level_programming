#!/bin/bash

for ((i=0; i<=99; i++))
do
    printf "%02d" $i

    if [ $i -ne 99 ]; then
        echo -n ", "
    else
        echo
    fi
done
