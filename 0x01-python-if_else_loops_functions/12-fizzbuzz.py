#!/bin/bash

fizzbuzz() {
    for ((i=1; i<=100; i++))
    do
        if [ $((i % 3)) -eq 0 ] && [ $((i % 5)) -eq 0 ]; then
            echo -n "FizzBuzz"
        elif [ $((i % 3)) -eq 0 ]; then
            echo -n "Fizz"
        elif [ $((i % 5)) -eq 0 ]; then
            echo -n "Buzz"
        else
            echo -n $i
        fi

        if [ $i -ne 100 ]; then
            echo -n " "
        else
            echo
        fi
    done
}

fizzbuzz
