#!/bin/bash

for char in {z..a}
do
    if [ $((i % 2)) -eq 0 ]; then
        echo -n ${char^^}
    else
        echo -n $char
    fi
done

echo
