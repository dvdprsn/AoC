#!/bin/bash

input="data/2022_1.txt"

readarray -t a < <(tr -d '\r' <$input)
declare -a sums
cur=0

for i in "${a[@]}"; do
    if [ -z ${i} ]; then
        sums+=($cur)
        cur=0
        continue
    fi
    cur=$(($i + $cur))
done

b=($(for l in ${sums[@]}; do echo $l; done | sort -n))
tot=$((b[-1] + b[-2] + b[-3]))
echo $tot
