#!/bin/bash/

echo "How many seconds?"

read seconds

echo "$seconds Seconds Timer Starts Now!"
for number in $(seq 1 120)
do
    echo $number
done


