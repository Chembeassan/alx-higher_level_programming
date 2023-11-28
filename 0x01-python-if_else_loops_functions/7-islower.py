#!/bin/bash

islower() {
    local char="$1"
    if [ "$char" == "$(echo -n $char | tr '[:upper:]' '[:lower:]')" ]; then
        return 0
    else
        return 1
    fi
}

echo "a is $(islower a && echo lower || echo upper)"
echo "H is $(islower H && echo lower || echo upper)"
echo "A is $(islower A && echo lower || echo upper)"
echo "3 is $(islower 3 && echo lower || echo upper)"
echo "g is $(islower g && echo lower || echo upper)"
