#!/bin/bash

for char in {a..z}
do
    if [ "$char" != "q" ] && [ "$char" != "e" ]; then
        echo -n $char
    fi
done

echo
