#!/bin/bash

print_last_digit() {
    local number="$1"
    echo $((number % 10))
}

print_last_digit 98
print_last_digit 0
r=$(print_last_digit -1024)
echo $r
