#!/bin/bash

number=$((RANDOM - RANDOM))

echo $number

if [ $number -gt 0 ]; then
    echo "is positive"
elif [ $number -eq 0 ]; then
    echo "is zero"
else
    echo "is negative"
fi
