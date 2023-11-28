#!/bin/bash

add() {
    local a="$1"
    local b="$2"
    echo $((a + b))
}

echo $(add 1 2)
echo $(add 98 0)
echo $(add 100 -2)
