#!/bin/bash

pow() {
    local a="$1"
    local b="$2"
    echo $((a ** b))
}

echo $(pow 2 2)
echo $(pow 98 2)
echo $(pow 98 0)
echo $(pow 100 -2)
echo $(pow -4 5)
