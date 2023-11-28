#!/bin/bash

number=$((RANDOM - RANDOM))

echo "Last digit of $number is $((number % 10)) and is" 

if [ $((number % 10)) -gt 5 ]; then
    echo "greater than 5"
elif [ $((number % 10)) -eq 0 ]; then
    echo "0"
else
    echo "less than 6 and not 0"
fi
