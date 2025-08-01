#!/usr/bin/env bash
echo "mi a helyzet?"
for i in $(seq 1 3);
do
    echo "$i"
done

read -p "a prompt ez: " valami
echo $valami