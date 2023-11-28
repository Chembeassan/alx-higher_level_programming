#!/bin/bash

uppercase() {
    local str="$1"
    echo $str | tr '[:lower:]' '[:upper:]'
}

uppercase "best"
uppercase "Best School 98 Battery street"
